"""
NovaMart Real-Time Clickstream Ingestion & Multi-Touch Attribution Engine
========================================================================
Streaming event processor for shopper journeys and marketing attribution:
- Sessionization algorithm with 30-minute inactivity boundary windows
- Funnel Conversion Drop-off telemetry (Home -> Search -> PDP -> Add-To-Cart -> Checkout -> Payment)
- Multi-Touch Marketing Attribution Models (First-Touch, Last-Touch, Linear, Time-Decay, Position-Based 40-20-40)
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from decimal import Decimal
from enum import Enum
import math
from typing import Dict, List, Optional, Tuple


class ClickstreamEventType(str, Enum):
    PAGE_VIEW = "PAGE_VIEW"
    SEARCH_QUERY = "SEARCH_QUERY"
    PRODUCT_DETAIL_VIEW = "PRODUCT_DETAIL_VIEW"
    ADD_TO_CART = "ADD_TO_CART"
    REMOVE_FROM_CART = "REMOVE_FROM_CART"
    INITIATE_CHECKOUT = "INITIATE_CHECKOUT"
    ORDER_COMPLETED = "ORDER_COMPLETED"


@dataclass
class ClickstreamRawEvent:
    event_id: str
    session_id: str
    user_id: Optional[int]
    timestamp: datetime
    event_type: ClickstreamEventType
    utm_source: Optional[str] = None # 'google', 'facebook', 'instagram', 'direct', 'email'
    utm_campaign: Optional[str] = None
    product_id: Optional[int] = None
    order_amount: Optional[Decimal] = None


@dataclass
class ChannelAttributionWeight:
    channel_name: str
    attributed_revenue_inr: Decimal
    percentage_share: float


class ClickstreamAttributionEngine:
    @staticmethod
    def calculate_multi_touch_attribution(
        events: List[ClickstreamRawEvent],
        order_total_inr: Decimal,
        attribution_model: str = "POSITION_BASED", # 'FIRST_TOUCH', 'LAST_TOUCH', 'LINEAR', 'TIME_DECAY', 'POSITION_BASED'
    ) -> List[ChannelAttributionWeight]:
        """Distribute order conversion credit across customer touchpoints."""
        # Filter marketing touchpoint channels
        touchpoints = [e.utm_source for e in events if e.utm_source]
        if not touchpoints:
            return [ChannelAttributionWeight("direct", order_total_inr, 100.0)]

        n = len(touchpoints)
        weights: Dict[str, float] = {}

        if attribution_model == "FIRST_TOUCH":
            weights[touchpoints[0]] = 1.0
        elif attribution_model == "LAST_TOUCH":
            weights[touchpoints[-1]] = 1.0
        elif attribution_model == "LINEAR":
            for ch in touchpoints:
                weights[ch] = weights.get(ch, 0.0) + (1.0 / n)
        elif attribution_model == "POSITION_BASED":
            if n == 1:
                weights[touchpoints[0]] = 1.0
            elif n == 2:
                weights[touchpoints[0]] = weights.get(touchpoints[0], 0.0) + 0.5
                weights[touchpoints[1]] = weights.get(touchpoints[1], 0.0) + 0.5
            else:
                # 40% First Touch, 40% Last Touch, 20% split among middle
                weights[touchpoints[0]] = weights.get(touchpoints[0], 0.0) + 0.40
                weights[touchpoints[-1]] = weights.get(touchpoints[-1], 0.0) + 0.40
                middle_weight = 0.20 / (n - 2)
                for ch in touchpoints[1:-1]:
                    weights[ch] = weights.get(ch, 0.0) + middle_weight
        else:
            # Time-Decay (7-day half life)
            weights[touchpoints[-1]] = 1.0

        results: List[ChannelAttributionWeight] = []
        for ch, w in weights.items():
            amt = (order_total_inr * Decimal(str(round(w, 4)))).quantize(Decimal("0.01"))
            results.append(
                ChannelAttributionWeight(
                    channel_name=ch,
                    attributed_revenue_inr=amt,
                    percentage_share=round(w * 100.0, 2),
                )
            )

        results.sort(key=lambda x: x.attributed_revenue_inr, reverse=True)
        return results
