"""create post table

Revision ID: 53a41eb9e560
Revises: 
Create Date: 2022-06-28 15:15:47.081715

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "53a41eb9e560"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("title", sa.String(), nullable=False),
    )
    pass


def downgrade() -> None:
    op.drop_table("posts")
    pass
