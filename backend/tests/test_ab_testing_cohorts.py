from datetime import datetime, timezone
import pytest

from app.services.ab_testing_engine import (
    ABExperiment,
    ABTestingEngine,
    ExperimentVariant,
)


def test_ab_testing_deterministic_bucketing():
    exp = ABExperiment(
        experiment_key="checkout_v2_redesign",
        description="Test 1-click buy button vs standard drawer",
        variants=[
            ExperimentVariant(variant_key="control", traffic_allocation_pct=50.0),
            ExperimentVariant(variant_key="variant_1click", traffic_allocation_pct=50.0),
        ],
        is_active=True,
        started_at=datetime.now(timezone.utc),
    )

    v_user1 = ABTestingEngine.assign_user_to_variant("user_1001", exp)
    v_user1_repeat = ABTestingEngine.assign_user_to_variant("user_1001", exp)
    assert v_user1 == v_user1_repeat # Deterministic persistence


def test_z_score_statistical_significance():
    # Control: 1000 visitors, 50 conversions (5.0%)
    # Variant: 1000 visitors, 85 conversions (8.5%)
    z, uplift_pct, is_sig = ABTestingEngine.calculate_two_proportion_z_score(
        n_control=1000,
        conv_control=50,
        n_variant=1000,
        conv_variant=85,
    )

    assert uplift_pct > 50.0 # 70% relative increase
    assert z > 1.96 # Statistically significant at p < 0.05
    assert is_sig is True
