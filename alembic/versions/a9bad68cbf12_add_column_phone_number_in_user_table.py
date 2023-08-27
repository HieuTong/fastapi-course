"""add column phone number in user table

Revision ID: a9bad68cbf12
Revises: 1921493c2ec0
Create Date: 2023-08-27 13:14:24.366094

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a9bad68cbf12'
down_revision: Union[str, None] = '1921493c2ec0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    pass


def downgrade() -> None:
    op.drop_column('users', 'phone_number')
    pass
