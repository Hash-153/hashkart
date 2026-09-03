from datetime import datetime, timezone
from typing import List, Optional
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models.helpdesk_qa import ProductAnswer, ProductQuestion
from app.models.order_payment import Order, OrderItem
from app.schemas.helpdesk_qa import (
    ProductAnswerCreate,
    ProductAnswerResponse,
    ProductQuestionCreate,
    ProductQuestionResponse,
)


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


async def get_product_questions(
    db: AsyncSession, product_id: int
) -> List[ProductQuestionResponse]:
    """Retrieve approved Q&A threads for a product, sorted by community upvotes."""
    stmt = (
        select(ProductQuestion)
        .options(
            selectinload(ProductQuestion.answers).selectinload(ProductAnswer.user),
            selectinload(ProductQuestion.user),
        )
        .where(
            ProductQuestion.product_id == product_id,
            ProductQuestion.is_approved == True,
        )
        .order_by(ProductQuestion.upvote_count.desc(), ProductQuestion.created_at.desc())
    )
    res = await db.execute(stmt)
    questions = res.scalars().all()

    results: List[ProductQuestionResponse] = []
    for q in questions:
        answers_resp = [
            ProductAnswerResponse(
                id=a.id,
                question_id=a.question_id,
                user_id=a.user_id,
                author_name=a.user.full_name if (a.user and a.user.full_name) else "Shopper",
                is_seller_answer=a.is_seller_answer,
                is_verified_buyer=a.is_verified_buyer,
                answer_text=a.answer_text,
                upvote_count=a.upvote_count,
                created_at=a.created_at,
            )
            for a in q.answers
            if a.is_approved
        ]
        results.append(
            ProductQuestionResponse(
                id=q.id,
                product_id=q.product_id,
                user_id=q.user_id,
                author_name=q.user.full_name if (q.user and q.user.full_name) else "Shopper",
                question_text=q.question_text,
                upvote_count=q.upvote_count,
                created_at=q.created_at,
                answers=answers_resp,
            )
        )

    return results


async def ask_product_question(
    db: AsyncSession, product_id: int, user_id: int, payload: ProductQuestionCreate
) -> ProductQuestion:
    """Post a customer question on a product detail page."""
    q = ProductQuestion(
        product_id=product_id,
        user_id=user_id,
        question_text=payload.question_text,
        is_approved=True,
        upvote_count=0,
    )
    db.add(q)
    await db.flush()
    await db.refresh(q)
    return q


async def answer_product_question(
    db: AsyncSession,
    question_id: int,
    user_id: int,
    payload: ProductAnswerCreate,
    is_seller: bool = False,
) -> ProductAnswer:
    """Submit an answer to a product question, checking for verified purchase status."""
    # Check if user purchased the product
    q_stmt = select(ProductQuestion).where(ProductQuestion.id == question_id)
    q_res = await db.execute(q_stmt)
    q = q_res.scalar_one_or_none()
    if not q:
        raise ValueError("Question not found")

    verified_buyer = False
    if not is_seller:
        # Check order history
        verify_stmt = (
            select(OrderItem)
            .join(Order)
            .where(
                Order.user_id == user_id,
                OrderItem.product_id == q.product_id,
            )
            .limit(1)
        )
        v_res = await db.execute(verify_stmt)
        if v_res.scalar_one_or_none():
            verified_buyer = True

    answer = ProductAnswer(
        question_id=question_id,
        user_id=user_id,
        answer_text=payload.answer_text,
        is_seller_answer=is_seller,
        is_verified_buyer=verified_buyer,
        is_approved=True,
        upvote_count=0,
    )
    db.add(answer)
    await db.flush()
    await db.refresh(answer)
    return answer


async def upvote_question(db: AsyncSession, question_id: int) -> int:
    """Increment upvote count for a question."""
    stmt = select(ProductQuestion).where(ProductQuestion.id == question_id)
    res = await db.execute(stmt)
    q = res.scalar_one_or_none()
    if q:
        q.upvote_count += 1
        await db.flush()
        return q.upvote_count
    return 0
