from decimal import Decimal
import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.catalog import Brand, Category, Product, ProductVariant
from app.schemas.helpdesk_qa import ProductAnswerCreate, ProductQuestionCreate
from app.services.comparison_service import generate_product_comparison_matrix
from app.services.qa_service import (
    answer_product_question,
    ask_product_question,
    get_product_questions,
    upvote_question,
)


@pytest.mark.asyncio
async def test_product_comparison_matrix(db_session: AsyncSession):
    """Test product spec comparison generation between multiple products."""
    cat = Category(name="Laptops", slug="laptops-cmp")
    b1 = Brand(name="Apple", slug="apple-cmp")
    b2 = Brand(name="Dell", slug="dell-cmp")
    db_session.add_all([cat, b1, b2])
    await db_session.flush()

    p1 = Product(name="MacBook Air M2", slug="macbook-air-m2", category_id=cat.id, brand_id=b1.id, description="Apple M2 chip laptop")
    p2 = Product(name="Dell XPS 13", slug="dell-xps-13", category_id=cat.id, brand_id=b2.id, description="Dell Intel Evo laptop")
    db_session.add_all([p1, p2])
    await db_session.flush()

    v1 = ProductVariant(product_id=p1.id, sku="MAC-M2-256", title="256GB SSD", price=Decimal("99990.00"), discount_price=Decimal("114900.00"), stock_quantity=10)
    v2 = ProductVariant(product_id=p2.id, sku="DELL-XPS-512", title="512GB SSD", price=Decimal("119990.00"), discount_price=Decimal("139990.00"), stock_quantity=10)
    db_session.add_all([v1, v2])
    await db_session.flush()

    matrix = await generate_product_comparison_matrix(db_session, [p1.id, p2.id])
    assert len(matrix.products) == 2
    assert matrix.category_name == "Laptops"
    assert len(matrix.spec_sections) >= 1


@pytest.mark.asyncio
async def test_product_qa_lifecycle(db_session: AsyncSession):
    """Test posting questions, answering, and upvoting."""
    cat = Category(name="Audio", slug="audio-qa")
    brand = Brand(name="Sony", slug="sony-qa")
    db_session.add_all([cat, brand])
    await db_session.flush()

    prod = Product(name="Sony WH-1000XM5", slug="sony-wh-1000xm5", category_id=cat.id, brand_id=brand.id, description="Industry leading noise cancellation")
    db_session.add(prod)
    await db_session.flush()

    variant = ProductVariant(product_id=prod.id, sku="SONY-XM5-BLK", title="Midnight Black", price=Decimal("26990.00"), stock_quantity=15)
    db_session.add(variant)
    await db_session.flush()

    # Ask question
    q_payload = ProductQuestionCreate(question_text="Does it support dual device bluetooth multipoint connection?")
    q = await ask_product_question(db_session, prod.id, user_id=1, payload=q_payload)
    assert q.id is not None

    # Answer question
    a_payload = ProductAnswerCreate(answer_text="Yes, you can connect to two devices simultaneously seamlessly.")
    ans = await answer_product_question(db_session, q.id, user_id=2, payload=a_payload, is_seller=True)
    assert ans.is_seller_answer is True

    # Upvote question
    upvotes = await upvote_question(db_session, q.id)
    assert upvotes == 1

    threads = await get_product_questions(db_session, prod.id)
    assert len(threads) == 1
    assert len(threads[0].answers) == 1
