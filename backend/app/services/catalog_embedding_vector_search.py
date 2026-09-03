"""
NovaMart Catalog Semantic Vector Indexer & HNSW Approximate Nearest Neighbor Engine
===================================================================================
High-dimensional dense vector embedding similarity search:
- Hierarchical Navigable Small World (HNSW) graph index construction
- Distance Metrics: Cosine Similarity, Inner Dot Product, Euclidean L2 Squared
- Multi-layer graph traversal with entry point routing and heuristic neighbor selection
- Product-to-Product visual & semantic similarity matching for cross-category recommendations
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
import math
import random
from typing import Dict, List, Optional, Set, Tuple


@dataclass
class VectorItem:
    item_id: int
    vector: List[float] # 128-dimensional dense semantic embedding
    metadata: Dict[str, any]


@dataclass
class HNSWGraphNode:
    item_id: int
    level: int
    neighbors_by_level: Dict[int, List[int]] = field(default_factory=dict)


class HNSWVectorIndex:
    def __init__(
        self,
        dimension: int = 128,
        m: int = 16, # Max outgoing links per node
        m0: int = 32, # Max outgoing links at level 0
        ef_construction: int = 64, # Size of dynamic candidate list during build
        ef_search: int = 32, # Size of dynamic candidate list during query
        ml: float = 1.0 / math.log(16), # Normalization factor for level generation
    ):
        self.dimension = dimension
        self.m = m
        self.m0 = m0
        self.ef_construction = ef_construction
        self.ef_search = ef_search
        self.ml = ml

        self.nodes: Dict[int, HNSWGraphNode] = {}
        self.vectors: Dict[int, List[float]] = {}
        self.enter_node_id: Optional[int] = None
        self.max_level: int = -1

    @staticmethod
    def cosine_similarity(v1: List[float], v2: List[float]) -> float:
        """Compute cosine similarity between two high-dimensional vectors."""
        dot = sum(a * b for a, b in zip(v1, v2))
        norm1 = math.sqrt(sum(a * a for a in v1))
        norm2 = math.sqrt(sum(b * b for b in v2))
        if norm1 == 0.0 or norm2 == 0.0:
            return 0.0
        return dot / (norm1 * norm2)

    @staticmethod
    def euclidean_distance_sq(v1: List[float], v2: List[float]) -> float:
        """Compute squared Euclidean distance."""
        return sum((a - b) ** 2 for a, b in zip(v1, v2))

    def _generate_random_level(self) -> int:
        """Draw level from exponential distribution."""
        unif = random.random()
        return int(-math.log(max(1e-9, unif)) * self.ml)

    def insert(self, item_id: int, vector: List[float]):
        """Insert vector into multi-layer HNSW graph."""
        self.vectors[item_id] = vector
        node_level = self._generate_random_level()
        new_node = HNSWGraphNode(item_id=item_id, level=node_level)
        for lev in range(node_level + 1):
            new_node.neighbors_by_level[lev] = []
        self.nodes[item_id] = new_node

        if self.enter_node_id is None:
            self.enter_node_id = item_id
            self.max_level = node_level
            return

        curr_obj = self.enter_node_id

        # Phase 1: Traverse from top layer down to node_level + 1
        for lev in range(self.max_level, node_level, -1):
            curr_obj = self._greedy_search_layer(curr_obj, vector, lev)

        # Phase 2: Link neighbors from min(max_level, node_level) down to 0
        top_link_level = min(self.max_level, node_level)
        for lev in range(top_link_level, -1, -1):
            candidates = self._search_layer_candidates(curr_obj, vector, self.ef_construction, lev)
            max_m = self.m0 if lev == 0 else self.m
            # Select top-M closest neighbors
            neighbors = sorted(candidates, key=lambda c: self.cosine_similarity(vector, self.vectors[c]), reverse=True)[:max_m]

            new_node.neighbors_by_level[lev] = neighbors
            for n_id in neighbors:
                n_node = self.nodes[n_id]
                if lev not in n_node.neighbors_by_level:
                    n_node.neighbors_by_level[lev] = []
                n_node.neighbors_by_level[lev].append(item_id)
                # Prune if exceeded max links
                if len(n_node.neighbors_by_level[lev]) > max_m:
                    n_vec = self.vectors[n_id]
                    n_node.neighbors_by_level[lev] = sorted(
                        n_node.neighbors_by_level[lev],
                        key=lambda cid: self.cosine_similarity(n_vec, self.vectors[cid]),
                        reverse=True,
                    )[:max_m]

            if candidates:
                curr_obj = neighbors[0]

        if node_level > self.max_level:
            self.max_level = node_level
            self.enter_node_id = item_id

    def _greedy_search_layer(self, enter_id: int, query_vec: List[float], level: int) -> int:
        curr_id = enter_id
        curr_sim = self.cosine_similarity(query_vec, self.vectors[curr_id])
        changed = True

        while changed:
            changed = False
            curr_node = self.nodes.get(curr_id)
            if not curr_node:
                break
            neighbors = curr_node.neighbors_by_level.get(level, [])
            for n_id in neighbors:
                n_sim = self.cosine_similarity(query_vec, self.vectors[n_id])
                if n_sim > curr_sim:
                    curr_sim = n_sim
                    curr_id = n_id
                    changed = True
                    break

        return curr_id

    def _search_layer_candidates(
        self, enter_id: int, query_vec: List[float], ef: int, level: int
    ) -> List[int]:
        visited: Set[int] = {enter_id}
        candidates: List[Tuple[float, int]] = [(self.cosine_similarity(query_vec, self.vectors[enter_id]), enter_id)]
        w_set: List[Tuple[float, int]] = [(self.cosine_similarity(query_vec, self.vectors[enter_id]), enter_id)]

        while candidates:
            candidates.sort(key=lambda x: x[0], reverse=True)
            curr_sim, curr_id = candidates.pop(0)

            # Check if current candidate is worse than furthest in W
            w_set.sort(key=lambda x: x[0])
            furthest_sim_in_w = w_set[0][0]

            if curr_sim < furthest_sim_in_w and len(w_set) >= ef:
                break

            curr_node = self.nodes.get(curr_id)
            if not curr_node:
                continue
            neighbors = curr_node.neighbors_by_level.get(level, [])

            for n_id in neighbors:
                if n_id not in visited:
                    visited.add(n_id)
                    n_sim = self.cosine_similarity(query_vec, self.vectors[n_id])

                    w_set.sort(key=lambda x: x[0])
                    if n_sim > w_set[0][0] or len(w_set) < ef:
                        candidates.append((n_sim, n_id))
                        w_set.append((n_sim, n_id))
                        if len(w_set) > ef:
                            w_set.sort(key=lambda x: x[0])
                            w_set.pop(0) # Remove furthest

        return [item[1] for item in w_set]

    def query_nearest_neighbors(
        self, query_vec: List[float], k: int = 10
    ) -> List[Tuple[int, float]]:
        """Search top-K nearest items using the hierarchical index."""
        if self.enter_node_id is None:
            return []

        curr_obj = self.enter_node_id
        for lev in range(self.max_level, 0, -1):
            curr_obj = self._greedy_search_layer(curr_obj, query_vec, lev)

        candidates = self._search_layer_candidates(curr_obj, query_vec, max(self.ef_search, k), 0)
        scored = [(c, self.cosine_similarity(query_vec, self.vectors[c])) for c in candidates]
        scored.sort(key=lambda x: x[1], reverse=True)
        return scored[:k]
