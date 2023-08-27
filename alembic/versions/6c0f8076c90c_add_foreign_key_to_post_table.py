"""add foreign key to post-table

Revision ID: 6c0f8076c90c
Revises: 3c6de7d73aff
Create Date: 2023-08-27 11:43:00.749546

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6c0f8076c90c'
down_revision: Union[str, None] = '3c6de7d73aff'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=[
        'owner_id'
    ], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint(
        'post_users_fk', table_name="posts"
    )
    op.drop_column('posts', 'owner_id')
    pass
