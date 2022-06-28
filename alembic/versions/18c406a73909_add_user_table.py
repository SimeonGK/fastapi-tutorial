"""add user table

Revision ID: 18c406a73909
Revises: 761555c279ce
Create Date: 2022-06-28 15:28:47.584201

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "18c406a73909"
down_revision = "761555c279ce"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    pass


def downgrade() -> None:
    op.drop_table("users")
    pass
