"""add content column to post table

Revision ID: 46356754160e
Revises: 66006fe27ca9
Create Date: 2023-08-26 05:48:53.889045

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '46356754160e'
down_revision: Union[str, None] = '66006fe27ca9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'posts', sa.Column('content', sa.String(), nullable=False)
    )
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
