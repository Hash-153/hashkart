"""Add warehouse pick and pack tasks.

Revision ID: 0003_fulfillment_tasks
Revises: 0002_operations
"""
from alembic import op
import sqlalchemy as sa

revision = "0003_fulfillment_tasks"
down_revision = "0002_operations"
branch_labels = None
depends_on = None


def upgrade() -> None:
    if sa.inspect(op.get_bind()).has_table("fulfillment_tasks"):
        return
    op.create_table(
        "fulfillment_tasks",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("order_id", sa.Integer(), sa.ForeignKey("orders.id", ondelete="CASCADE"), nullable=False),
        sa.Column("shipment_id", sa.Integer(), sa.ForeignKey("shipments.id", ondelete="SET NULL")),
        sa.Column("task_type", sa.String(20), nullable=False),
        sa.Column("status", sa.String(20), nullable=False),
        sa.Column("assigned_to", sa.Integer(), sa.ForeignKey("users.id", ondelete="SET NULL")),
        sa.Column("notes", sa.Text()),
        sa.Column("started_at", sa.DateTime()),
        sa.Column("completed_at", sa.DateTime()),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.UniqueConstraint("order_id", "task_type", name="uq_order_fulfillment_task_type"),
    )


def downgrade() -> None:
    op.drop_table("fulfillment_tasks")
