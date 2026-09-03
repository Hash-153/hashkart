import re
from typing import List, Tuple, Dict, Any, Optional, Set


class SearchService:
    """Text normalization, tokenization, search relevance scoring, and typo correction engine."""

    @staticmethod
    def normalize_query(query: str) -> str:
        """
        Normalize query string:
        - Lowercase
        - Replace punctuation with spaces
        - Collapse multiple spaces
        - Trim whitespace
        """
        if not query:
            return ""
        text = query.lower()
        text = re.sub(r"[^\w\s]", " ", text)
        text = re.sub(r"\s+", " ", text)
        return text.strip()

    @staticmethod
    def stem_token(token: str) -> str:
        """Lightweight plural stemming for common search tokens."""
        if len(token) > 4 and token.endswith("ies"):
            return token[:-3] + "y"
        if len(token) > 4 and token.endswith("s") and not token.endswith("ss"):
            return token[:-1]
        return token

    @staticmethod
    def tokenize(query: str) -> List[str]:
        """Split normalized query into distinct search terms (tokens length >= 2)."""
        normalized = SearchService.normalize_query(query)
        if not normalized:
            return []
        raw_tokens = [t for t in normalized.split(" ") if len(t) >= 2]
        stemmed_tokens = []
        for t in raw_tokens:
            if t not in stemmed_tokens:
                stemmed_tokens.append(t)
            stemmed = SearchService.stem_token(t)
            if stemmed not in stemmed_tokens:
                stemmed_tokens.append(stemmed)
        return stemmed_tokens

    @staticmethod
    def lev_distance(s1: str, s2: str) -> int:
        """Calculate Levenshtein distance between two strings."""
        if len(s1) < len(s2):
            return SearchService.lev_distance(s2, s1)
        if len(s2) == 0:
            return len(s1)

        previous_row = range(len(s2) + 1)
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row
        return previous_row[-1]

    @staticmethod
    def calculate_relevance_score(
        query_raw: str,
        product_name: str,
        sku_list: List[str],
        brand_name: Optional[str] = None,
        category_name: Optional[str] = None,
        description: Optional[str] = None,
        attributes_list: Optional[List[str]] = None,
    ) -> Tuple[float, List[str]]:
        """
        Calculate weighted search relevance score and return match explanation tags.
        Match tags: SKU_MATCH, NAME_EXACT, NAME_PREFIX, BRAND_MATCH, CATEGORY_MATCH, ATTRIBUTE_MATCH, DESCRIPTION_MATCH.
        """
        norm_q = SearchService.normalize_query(query_raw)
        if not norm_q:
            return 0.0, []

        tokens = SearchService.tokenize(query_raw)
        score = 0.0
        reasons: Set[str] = set()

        norm_name = SearchService.normalize_query(product_name)
        norm_brand = SearchService.normalize_query(brand_name or "")
        norm_cat = SearchService.normalize_query(category_name or "")
        norm_desc = SearchService.normalize_query(description or "")
        norm_attrs = [SearchService.normalize_query(a) for a in (attributes_list or [])]

        # 1. SKU Match
        for sku in sku_list:
            norm_sku = SearchService.normalize_query(sku)
            if norm_q == norm_sku:
                score += 100.0
                reasons.add("SKU_MATCH")
            elif norm_q in norm_sku:
                score += 50.0
                reasons.add("SKU_MATCH")

        # 2. Product Name Match
        if norm_q == norm_name:
            score += 80.0
            reasons.add("NAME_EXACT")
        elif norm_name.startswith(norm_q):
            score += 50.0
            reasons.add("NAME_PREFIX")

        for token in tokens:
            if token in norm_name:
                score += 30.0
                reasons.add("NAME_MATCH")
            if norm_brand and token in norm_brand:
                score += 25.0
                reasons.add("BRAND_MATCH")
            if norm_cat and token in norm_cat:
                score += 15.0
                reasons.add("CATEGORY_MATCH")
            if norm_desc and token in norm_desc:
                score += 5.0
                reasons.add("DESCRIPTION_MATCH")
            for attr_val in norm_attrs:
                if token in attr_val:
                    score += 20.0
                    reasons.add("ATTRIBUTE_MATCH")

        return score, list(reasons)

    @staticmethod
    def generate_did_you_mean(query: str, vocabulary: Set[str]) -> Optional[str]:
        """
        Generate a "Did You Mean?" suggestion if a token has a close edit distance (distance <= 2)
        against catalog vocabulary terms.
        """
        tokens = query.strip().split(" ")
        corrected_tokens = []
        changed = False

        for token in tokens:
            norm_t = SearchService.normalize_query(token)
            if not norm_t or len(norm_t) < 3 or norm_t in vocabulary:
                corrected_tokens.append(token)
                continue

            # Find best vocabulary match with Levenshtein distance <= 2
            best_word = None
            best_dist = 999
            for word in vocabulary:
                if abs(len(word) - len(norm_t)) > 2:
                    continue
                dist = SearchService.lev_distance(norm_t, word)
                if dist <= 2 and dist < best_dist:
                    best_dist = dist
                    best_word = word

            if best_word and best_dist > 0:
                corrected_tokens.append(best_word)
                changed = True
            else:
                corrected_tokens.append(token)

        return " ".join(corrected_tokens) if changed else None
