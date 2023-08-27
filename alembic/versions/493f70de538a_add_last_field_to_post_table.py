"""add last field to post table

Revision ID: 493f70de538a
Revises: 6c0f8076c90c
Create Date: 2023-08-27 11:52:19.993814

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '493f70de538a'
down_revision: Union[str, None] = '6c0f8076c90c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column(
    'posts', 'published'
    )
    op.drop_column(
        'posts', 'created_at'
    )
    pass
