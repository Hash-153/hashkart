from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func

from app.database import get_db
from app.models.promotion_review import Review
from app.models.order_payment import Order, OrderItem
from app.models.catalog import Product
from app.models.user import User
from app.schemas.promotion_review import ReviewCreate, ReviewResponse
from app.core.deps import get_current_user

router = APIRouter()


@router.get("/product/{product_id}", response_model=List[ReviewResponse])
async def get_product_reviews(product_id: int, db: AsyncSession = Depends(get_db)):
    """Fetch approved product reviews and ratings."""
    result = await db.execute(
        select(Review)
        .where(Review.product_id == product_id, Review.status == "APPROVED")
        .order_by(Review.created_at.desc())
    )
    reviews = result.scalars().all()
    
    response = []
    for r in reviews:
        item = ReviewResponse.model_validate(r)
        item.user_name = r.user.full_name if r.user else "Verified Customer"
        response.append(item)
    return response


@router.post("", response_model=ReviewResponse, status_code=status.HTTP_201_CREATED)
async def create_review(
    review_in: ReviewCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Submit a written product review and star rating (verifies purchase)."""
    # Verify product exists
    prod_res = await db.execute(select(Product).where(Product.id == review_in.product_id))
    product = prod_res.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found.")

    # Check verified purchase flag
    purchase_stmt = (
        select(OrderItem)
        .join(Order)
        .where(
            Order.user_id == current_user.id,
            Order.status == "DELIVERED",
            OrderItem.variant_id == review_in.variant_id if review_in.variant_id else True,
        )
    )
    purchase_res = await db.execute(purchase_stmt)
    is_verified = len(purchase_res.scalars().all()) > 0

    new_review = Review(
        product_id=review_in.product_id,
        user_id=current_user.id,
        variant_id=review_in.variant_id,
        rating=review_in.rating,
        title=review_in.title,
        comment=review_in.comment,
        is_verified_purchase=is_verified,
        status="APPROVED",  # Auto-approve for local dev
    )
    db.add(new_review)
    await db.flush()

    # Recalculate average product rating
    rating_stmt = select(
        func.avg(Review.rating), func.count(Review.id)
    ).where(Review.product_id == review_in.product_id, Review.status == "APPROVED")
    rating_res = await db.execute(rating_stmt)
    avg_rating, count = rating_res.first()

    product.rating_avg = round(float(avg_rating or 0.0), 1)
    product.review_count = count or 0

    await db.commit()
    await db.refresh(new_review)

    res = ReviewResponse.model_validate(new_review)
    res.user_name = current_user.full_name
    return res
