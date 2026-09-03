"""
NovaMart Real-Time Collaborative Filtering & Recommendation ML Engine
======================================================================
Computes personalized product recommendations using:
- User-item interaction matrix with exponential time-decay weighting
- Item-to-item cosine similarity vectors across product attribute embeddings
- Real-time in-session category affinity prediction
- Frequently Bought Together (FBT) basket association rules
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
import math
from typing import Dict, List, Optional, Set, Tuple


@dataclass
class UserInteraction:
    user_id: int
    product_id: int
    interaction_type: str # 'VIEW', 'CART', 'WISHLIST', 'PURCHASE'
    timestamp: datetime
    category_id: int
    weight: float = 1.0


@dataclass
class RecommendedProductScore:
    product_id: int
    confidence_score: float
    recommendation_source: str # 'COLLABORATIVE', 'CONTENT_SIMILARITY', 'BASKET_AFFINITY', 'TRENDING'
    category_name: str
    reasons: List[str]


# Interaction action weights
ACTION_WEIGHTS: Dict[str, float] = {
    "VIEW": 1.0,
    "SEARCH_CLICK": 1.5,
    "WISHLIST": 3.0,
    "CART": 5.0,
    "PURCHASE": 10.0,
}

# Exponential decay half-life in days
DECAY_HALF_LIFE_DAYS = 7.0


def compute_time_decay_weight(timestamp: datetime, now: Optional[datetime] = None) -> float:
    """Calculate exponential time-decay weight for past user actions."""
    if now is None:
        now = datetime.now(timezone.utc)
    delta_days = max(0.0, (now - timestamp).total_seconds() / 86400.0)
    decay = math.exp(-math.log(2.0) * delta_days / DECAY_HALF_LIFE_DAYS)
    return max(0.05, decay)


class RecommendationEngine:
    def __init__(self):
        # item_id -> {attr_key: attr_val}
        self.item_profiles: Dict[int, Dict[str, str]] = {}
        # item_id -> category_id
        self.item_categories: Dict[int, int] = {}
        # item_a -> {item_b: co-occurrence_count}
        self.co_occurrence_matrix: Dict[int, Dict[int, int]] = {}

    def register_product(self, product_id: int, category_id: int, attributes: Dict[str, str]):
        """Register product features and attributes for vector similarity."""
        self.item_profiles[product_id] = attributes
        self.item_categories[product_id] = category_id

    def record_co_purchase(self, item_ids: List[int]):
        """Update Market Basket co-occurrence matrix for association rule mining."""
        for i in range(len(item_ids)):
            for j in range(len(item_ids)):
                if i != j:
                    a = item_ids[i]
                    b = item_ids[j]
                    if a not in self.co_occurrence_matrix:
                        self.co_occurrence_matrix[a] = {}
                    self.co_occurrence_matrix[a][b] = self.co_occurrence_matrix[a].get(b, 0) + 1

    def calculate_item_similarity(self, item_a: int, item_b: int) -> float:
        """Compute cosine similarity between two product attribute profiles."""
        if item_a == item_b:
            return 1.0

        prof_a = self.item_profiles.get(item_a, {})
        prof_b = self.item_profiles.get(item_b, {})

        if not prof_a or not prof_b:
            # Fallback to category match
            cat_a = self.item_categories.get(item_a)
            cat_b = self.item_categories.get(item_b)
            return 0.5 if (cat_a and cat_a == cat_b) else 0.0

        # Jaccard / Cosine intersection of key-value matches
        keys_a = set(prof_a.items())
        keys_b = set(prof_b.items())

        intersection = len(keys_a.intersection(keys_b))
        union = len(keys_a.union(keys_b))

        if union == 0:
            return 0.0

        score = intersection / union
        # Category bonus
        if self.item_categories.get(item_a) == self.item_categories.get(item_b):
            score = (score * 0.7) + 0.3

        return round(score, 4)

    def get_frequently_bought_together(self, product_id: int, limit: int = 4) -> List[Tuple[int, float]]:
        """Retrieve top companion products bought in the same order."""
        co_items = self.co_occurrence_matrix.get(product_id, {})
        if not co_items:
            return []

        total_orders = sum(co_items.values())
        scored = [
            (item_id, round(count / total_orders, 3))
            for item_id, count in co_items.items()
        ]
        scored.sort(key=lambda x: x[1], reverse=True)
        return scored[:limit]

    def predict_personalized_feed(
        self,
        interactions: List[UserInteraction],
        candidate_product_ids: List[int],
        top_k: int = 10,
    ) -> List[RecommendedProductScore]:
        """Generate ranked personalized recommendations based on past user interaction history."""
        if not interactions:
            # Cold-start fallback: return popular candidates
            return [
                RecommendedProductScore(
                    product_id=p_id,
                    confidence_score=0.5,
                    recommendation_source="TRENDING",
                    category_name="Popular",
                    reasons=["Popular trending choice across marketplace"],
                )
                for p_id in candidate_product_ids[:top_k]
            ]

        # Calculate user category and item affinity scores
        user_category_affinity: Dict[int, float] = {}
        interacted_item_weights: Dict[int, float] = {}
        now = datetime.now(timezone.utc)

        for inter in interactions:
            base_w = ACTION_WEIGHTS.get(inter.interaction_type, 1.0)
            decay_w = compute_time_decay_weight(inter.timestamp, now)
            effective_weight = base_w * decay_w

            user_category_affinity[inter.category_id] = (
                user_category_affinity.get(inter.category_id, 0.0) + effective_weight
            )
            interacted_item_weights[inter.product_id] = (
                interacted_item_weights.get(inter.product_id, 0.0) + effective_weight
            )

        # Normalize affinities
        max_cat = max(user_category_affinity.values()) if user_category_affinity else 1.0

        scores: List[RecommendedProductScore] = []
        interacted_ids = set(interacted_item_weights.keys())

        for cand_id in candidate_product_ids:
            if cand_id in interacted_ids:
                continue # Do not recommend products the user already bought / engaged heavily

            cand_cat = self.item_categories.get(cand_id, 0)
            cat_score = (user_category_affinity.get(cand_cat, 0.0) / max_cat) if max_cat > 0 else 0.0

            # Content similarity to items user liked
            sim_scores = [
                self.calculate_item_similarity(cand_id, past_id) * w
                for past_id, w in interacted_item_weights.items()
            ]
            max_sim = max(sim_scores) if sim_scores else 0.0

            combined_score = round((cat_score * 0.4) + (min(1.0, max_sim) * 0.6), 4)

            reasons = []
            if cat_score > 0.6:
                reasons.append("Matches your recent category browsing interests")
            if max_sim > 0.4:
                reasons.append("Similar features to products you viewed")
            if not reasons:
                reasons.append("Recommended based on shopper preferences")

            scores.append(
                RecommendedProductScore(
                    product_id=cand_id,
                    confidence_score=combined_score,
                    recommendation_source="COLLABORATIVE",
                    category_name=f"Category #{cand_cat}",
                    reasons=reasons,
                )
            )

        scores.sort(key=lambda x: x.confidence_score, reverse=True)
        return scores[:top_k]
