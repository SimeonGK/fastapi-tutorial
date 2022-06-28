"""add content column to posts table

Revision ID: 761555c279ce
Revises: 53a41eb9e560
Create Date: 2022-06-28 15:24:36.601568

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "761555c279ce"
down_revision = "53a41eb9e560"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
