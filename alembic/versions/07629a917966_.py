"""empty message

Revision ID: 07629a917966
Revises: 493f70de538a
Create Date: 2023-08-27 12:10:46.188647

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '07629a917966'
down_revision: Union[str, None] = '493f70de538a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
