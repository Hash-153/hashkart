from decimal import Decimal
import pytest

from app.services.seller_advertising_engine import (
    AdKeywordBid,
    SponsoredAdCampaign,
    SponsoredAdsEngine,
)


def test_sponsored_ads_gsp_auction():
    # Campaign 1: High bid ₹15.00, quality score 9.0
    c1 = SponsoredAdCampaign(
        campaign_id=1,
        seller_id=10,
        product_id=101,
        campaign_name="iPhone 15 Campaign",
        daily_budget=Decimal("500.00"),
        spent_today=Decimal("50.00"),
        bids=[AdKeywordBid(keyword="iphone 15", match_type="EXACT", max_cpc_bid=Decimal("15.00"))],
        quality_score=9.0,
        is_active=True,
    )

    # Campaign 2: Lower bid ₹10.00, quality score 8.0
    c2 = SponsoredAdCampaign(
        campaign_id=2,
        seller_id=20,
        product_id=202,
        campaign_name="Galaxy S24 Campaign",
        daily_budget=Decimal("500.00"),
        spent_today=Decimal("20.00"),
        bids=[AdKeywordBid(keyword="iphone", match_type="BROAD", max_cpc_bid=Decimal("10.00"))],
        quality_score=8.0,
        is_active=True,
    )

    res = SponsoredAdsEngine.run_cpc_auction("iphone 15", [c1, c2], max_ad_slots=2)
    assert len(res.sponsored_product_ids) == 2
    assert res.sponsored_product_ids[0] == 101 # Campaign 1 wins 1st slot
    assert res.charged_cpcs_by_product_id[101] <= Decimal("15.00") # Second price rule charged
