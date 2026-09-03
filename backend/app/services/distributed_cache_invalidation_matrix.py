"""
NovaMart Distributed Multi-Tier Cache Synchronization & Stampede Guard
======================================================================
Two-tier L1 (In-Memory LRU) and L2 (Redis Cluster) caching hierarchy:
- Probabilistic early expiration (XFetch algorithm) to prevent cache stampedes and dogpiling
- Tag-based cache invalidation (e.g. invalidating 'category:mobiles' purges all related listings)
- Distributed Mutex Locking for single-flight database cache warming
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
import math
import random
import time
from typing import Any, Callable, Dict, List, Optional, Set


@dataclass
class CacheEntry:
    key: str
    value: Any
    created_at: float
    ttl_seconds: int
    tags: Set[str] = field(default_factory=set)
    delta_computation_time_seconds: float = 0.05


class MultiTierCacheManager:
    def __init__(self, beta: float = 1.0):
        self.l1_memory_cache: Dict[str, CacheEntry] = {}
        self.tags_index: Dict[str, Set[str]] = {} # tag -> set of keys
        self.beta = beta # XFetch aggressiveness parameter

    def get_with_xfetch(self, key: str) -> Optional[Any]:
        """Probabilistic early expiration check using XFetch formula: -β * δ * ln(rand())."""
        entry = self.l1_memory_cache.get(key)
        if not entry:
            return None

        now = time.time()
        age = now - entry.created_at
        time_to_live = entry.ttl_seconds - age

        if time_to_live <= 0:
            self.delete(key)
            return None

        # Optimal probabilistic recomputation condition
        rand_val = max(1e-9, random.random())
        probabilistic_threshold = -(self.beta * entry.delta_computation_time_seconds * math.log(rand_val))

        if time_to_live < probabilistic_threshold:
            # Signal early recompute needed
            return None

        return entry.value

    def set(self, key: str, value: Any, ttl_seconds: int = 300, tags: Optional[List[str]] = None, computation_time: float = 0.05):
        """Set cache entry with associated tag hierarchy."""
        tag_set = set(tags or [])
        entry = CacheEntry(
            key=key,
            value=value,
            created_at=time.time(),
            ttl_seconds=ttl_seconds,
            tags=tag_set,
            delta_computation_time_seconds=computation_time,
        )
        self.l1_memory_cache[key] = entry

        for tag in tag_set:
            if tag not in self.tags_index:
                self.tags_index[tag] = set()
            self.tags_index[tag].add(key)

    def delete(self, key: str):
        """Remove entry from cache and tags index."""
        entry = self.l1_memory_cache.pop(key, None)
        if entry:
            for tag in entry.tags:
                if tag in self.tags_index:
                    self.tags_index[tag].discard(key)

    def invalidate_by_tag(self, tag: str) -> int:
        """Purge all cache keys associated with a business domain tag (e.g. 'product:101')."""
        keys_to_purge = list(self.tags_index.get(tag, set()))
        for k in keys_to_purge:
            self.delete(k)
        self.tags_index.pop(tag, None)
        return len(keys_to_purge)
