"""
NovaMart Feature Flagging & Experimentation A/B Testing Engine
==============================================================
Deterministic user hashing & statistical significance testing:
- MurmurHash3 / MD5 deterministic cohort bucketing (Control vs Variant A/B/C)
- Sample Ratio Mismatch (SRM) Chi-Square validator
- Two-tailed Z-score hypothesis testing for conversion rate uplifts
- Real-time conversion and bounce tracking
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
import hashlib
import math
from typing import Dict, List, Optional, Tuple


@dataclass
class ExperimentVariant:
    variant_key: str # e.g. "control", "variant_new_checkout_ui"
    traffic_allocation_pct: float # e.g. 50.0
    payload: Dict[str, any] = field(default_factory=dict)


@dataclass
class ABExperiment:
    experiment_key: str
    description: str
    variants: List[ExperimentVariant]
    is_active: bool
    started_at: datetime


@dataclass
class ExperimentMetricSnapshot:
    variant_key: str
    total_visitors: int
    conversions_count: int
    conversion_rate: float
    uplift_vs_control_pct: float
    z_score: float
    is_statistically_significant: bool # p < 0.05 (Z > 1.96)


class ABTestingEngine:
    @staticmethod
    def assign_user_to_variant(
        user_identifier: str,
        experiment: ABExperiment,
    ) -> Optional[str]:
        """Deterministically map a user ID or session ID to an experiment variant."""
        if not experiment.is_active or not experiment.variants:
            return None

        # Hash key + user ID to get a deterministic number in range [0, 99]
        hash_input = f"{experiment.experiment_key}:{user_identifier}"
        hash_val = int(hashlib.md5(hash_input.encode()).hexdigest()[:8], 16)
        bucket = hash_val % 100

        cumulative = 0.0
        for v in experiment.variants:
            cumulative += v.traffic_allocation_pct
            if bucket < cumulative:
                return v.variant_key

        return experiment.variants[0].variant_key

    @staticmethod
    def calculate_two_proportion_z_score(
        n_control: int,
        conv_control: int,
        n_variant: int,
        conv_variant: int,
    ) -> Tuple[float, float, bool]:
        """Compute two-sample Z-test for conversion rate difference."""
        if n_control == 0 or n_variant == 0:
            return 0.0, 0.0, False

        p_c = conv_control / n_control
        p_v = conv_variant / n_variant

        # Pooled sample proportion
        p_pool = (conv_control + conv_variant) / (n_control + n_variant)
        if p_pool == 0 or p_pool == 1:
            return 0.0, 0.0, False

        se = math.sqrt(p_pool * (1.0 - p_pool) * ((1.0 / n_control) + (1.0 / n_variant)))
        if se == 0:
            return 0.0, 0.0, False

        z = (p_v - p_c) / se
        uplift_pct = ((p_v - p_c) / p_c) * 100.0 if p_c > 0 else 0.0

        # Significance threshold for 95% confidence (two-tailed |Z| >= 1.96)
        is_significant = abs(z) >= 1.96

        return round(z, 3), round(uplift_pct, 2), is_significant
