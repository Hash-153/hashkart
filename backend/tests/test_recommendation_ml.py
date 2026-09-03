from datetime import datetime, timedelta, timezone
import pytest

from app.services.recommendation_ml import (
    RecommendationEngine,
    UserInteraction,
    compute_time_decay_weight,
)


def test_time_decay_weight_calculation():
    now = datetime.now(timezone.utc)
    w_today = compute_time_decay_weight(now, now)
    assert w_today == 1.0

    w_7_days_ago = compute_time_decay_weight(now - timedelta(days=7), now)
    assert abs(w_7_days_ago - 0.5) < 0.05

    w_30_days_ago = compute_time_decay_weight(now - timedelta(days=30), now)
    assert w_30_days_ago < 0.2


def test_recommendation_engine_cosine_and_collaborative_feed():
    engine = RecommendationEngine()

    # Register catalog products
    engine.register_product(1, category_id=10, attributes={"brand": "Apple", "storage": "128GB", "os": "iOS"})
    engine.register_product(2, category_id=10, attributes={"brand": "Apple", "storage": "256GB", "os": "iOS"})
    engine.register_product(3, category_id=10, attributes={"brand": "Samsung", "storage": "256GB", "os": "Android"})
    engine.register_product(4, category_id=20, attributes={"brand": "Sony", "type": "Headphones"})

    # Check similarity
    sim_1_2 = engine.calculate_item_similarity(1, 2)
    sim_1_4 = engine.calculate_item_similarity(1, 4)
    assert sim_1_2 > sim_1_4

    # Co-occurrence
    engine.record_co_purchase([1, 4])
    fbt = engine.get_frequently_bought_together(1)
    assert len(fbt) == 1
    assert fbt[0][0] == 4

    # User interactions: User viewed and carted Apple product
    now = datetime.now(timezone.utc)
    interactions = [
        UserInteraction(user_id=99, product_id=1, interaction_type="CART", timestamp=now, category_id=10),
    ]

    feed = engine.predict_personalized_feed(interactions, candidate_product_ids=[2, 3, 4], top_k=2)
    assert len(feed) == 2
    # Product 2 (similar Apple product in same category) should rank first
    assert feed[0].product_id == 2
    assert feed[0].confidence_score > 0.5
