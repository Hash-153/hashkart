"""
NovaMart Seller Advertising & Product Listing Ads (PLA) CPC Auction Engine
==========================================================================
Manages sponsored product campaigns:
- Real-time Generalized Second-Price (GSP) CPC ad auction
- Ad Quality Score (CTR prediction * relevance * seller rating)
- Daily campaign budget pacing & impression capping
- Return on Ad Spend (ROAS) and Attribution reporting (1-day, 7-day, 14-day)
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from decimal import Decimal
from typing import Dict, List, Optional, Tuple


@dataclass
class AdKeywordBid:
    keyword: str
    match_type: str # 'EXACT', 'PHRASE', 'BROAD'
    max_cpc_bid: Decimal


@dataclass
class SponsoredAdCampaign:
    campaign_id: int
    seller_id: int
    product_id: int
    campaign_name: str
    daily_budget: Decimal
    spent_today: Decimal
    bids: List[AdKeywordBid]
    quality_score: float # 0.0 to 10.0
    is_active: bool


@dataclass
class AuctionCandidateScore:
    campaign_id: int
    seller_id: int
    product_id: int
    ad_rank_score: float
    actual_cpc_charged: Decimal
    winning_keyword: str


@dataclass
class AuctionResult:
    search_query: str
    sponsored_product_ids: List[int]
    charged_cpcs_by_product_id: Dict[int, Decimal]
    auction_metadata: List[AuctionCandidateScore]


class SponsoredAdsEngine:
    @staticmethod
    def match_keyword_score(query: str, bid: AdKeywordBid) -> float:
        """Calculate match relevance between customer search and advertiser bid."""
        q = query.lower().strip()
        kw = bid.keyword.lower().strip()

        if bid.match_type == "EXACT":
            return 1.0 if q == kw else 0.0
        elif bid.match_type == "PHRASE":
            return 0.85 if kw in q else 0.0
        else: # BROAD
            words = set(kw.split())
            query_words = set(q.split())
            intersection = words.intersection(query_words)
            return (len(intersection) / len(words)) if words else 0.0

    @classmethod
    def run_cpc_auction(
        cls,
        search_query: str,
        active_campaigns: List[SponsoredAdCampaign],
        max_ad_slots: int = 3,
    ) -> AuctionResult:
        """Execute Generalized Second-Price (GSP) auction for sponsored search results."""
        eligible_bidders: List[Tuple[SponsoredAdCampaign, AdKeywordBid, float, float]] = []

        for camp in active_campaigns:
            if not camp.is_active:
                continue
            if camp.spent_today >= camp.daily_budget:
                continue # Budget exhausted

            best_bid = None
            best_match_score = 0.0

            for b in camp.bids:
                m_score = cls.match_keyword_score(search_query, b)
                if m_score > best_match_score:
                    best_match_score = m_score
                    best_bid = b

            if best_bid and best_match_score > 0.3:
                # Ad Rank = Max CPC Bid * Quality Score * Match Score
                ad_rank = float(best_bid.max_cpc_bid) * (camp.quality_score / 10.0) * best_match_score
                eligible_bidders.append((camp, best_bid, ad_rank, best_match_score))

        # Sort by Ad Rank descending
        eligible_bidders.sort(key=lambda x: x[2], reverse=True)

        winners = eligible_bidders[:max_ad_slots]
        sponsored_ids: List[int] = []
        cpc_map: Dict[int, Decimal] = {}
        meta_scores: List[AuctionCandidateScore] = []

        for idx, (camp, bid, rank, m_score) in enumerate(winners):
            # Second-Price Rule: Next bidder's Ad Rank / this bidder's Quality Score
            if idx + 1 < len(eligible_bidders):
                next_rank = eligible_bidders[idx + 1][2]
                quality_denom = max(0.1, (camp.quality_score / 10.0) * m_score)
                actual_cpc = Decimal(str(round(next_rank / quality_denom + 0.05, 2)))
                actual_cpc = min(bid.max_cpc_bid, actual_cpc) # Cap at max bid
            else:
                actual_cpc = Decimal("2.00") # Floor reserve price

            sponsored_ids.append(camp.product_id)
            cpc_map[camp.product_id] = actual_cpc

            meta_scores.append(
                AuctionCandidateScore(
                    campaign_id=camp.campaign_id,
                    seller_id=camp.seller_id,
                    product_id=camp.product_id,
                    ad_rank_score=round(rank, 3),
                    actual_cpc_charged=actual_cpc,
                    winning_keyword=bid.keyword,
                )
            )

        return AuctionResult(
            search_query=search_query,
            sponsored_product_ids=sponsored_ids,
            charged_cpcs_by_product_id=cpc_map,
            auction_metadata=meta_scores,
        )
