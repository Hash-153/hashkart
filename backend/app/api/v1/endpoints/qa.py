from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.deps import get_current_user, get_db
from app.models.user import User
from app.schemas.helpdesk_qa import (
    ProductAnswerCreate,
    ProductAnswerResponse,
    ProductQuestionCreate,
    ProductQuestionResponse,
)
from app.services.qa_service import (
    answer_product_question,
    ask_product_question,
    get_product_questions,
    upvote_question,
)

router = APIRouter()


@router.get("/products/{product_id}/questions", response_model=List[ProductQuestionResponse])
async def list_product_qa_threads(
    product_id: int,
    db: AsyncSession = Depends(get_db),
):
    """Retrieve community Questions and Answers for a product on its PDP."""
    return await get_product_questions(db, product_id)


@router.post("/products/{product_id}/questions", response_model=ProductQuestionResponse)
async def post_product_question(
    product_id: int,
    payload: ProductQuestionCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Post a new question about a product."""
    q = await ask_product_question(db, product_id, current_user.id, payload)
    await db.commit()

    return ProductQuestionResponse(
        id=q.id,
        product_id=q.product_id,
        user_id=q.user_id,
        author_name=current_user.full_name or "Shopper",
        question_text=q.question_text,
        upvote_count=0,
        created_at=q.created_at,
        answers=[],
    )


@router.post("/questions/{question_id}/answers", response_model=ProductAnswerResponse)
async def post_question_answer(
    question_id: int,
    payload: ProductAnswerCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Post an answer to a product question."""
    is_seller = any(r.name == "SELLER" for r in (current_user.roles or []))
    ans = await answer_product_question(db, question_id, current_user.id, payload, is_seller=is_seller)
    await db.commit()

    return ProductAnswerResponse(
        id=ans.id,
        question_id=ans.question_id,
        user_id=ans.user_id,
        author_name=current_user.full_name or "Shopper",
        is_seller_answer=ans.is_seller_answer,
        is_verified_buyer=ans.is_verified_buyer,
        answer_text=ans.answer_text,
        upvote_count=0,
        created_at=ans.created_at,
    )


@router.post("/questions/{question_id}/upvote")
async def upvote_qa_question(
    question_id: int,
    db: AsyncSession = Depends(get_db),
):
    """Upvote a helpful product question."""
    new_count = await upvote_question(db, question_id)
    await db.commit()
    return {"question_id": question_id, "upvotes": new_count}
