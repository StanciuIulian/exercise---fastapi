"""add foreign-key to post table

Revision ID: e7752421ef5a
Revises: 707ffab0cd1d
Create Date: 2024-11-17 18:23:00.245652

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e7752421ef5a'
down_revision: Union[str, None] = '707ffab0cd1d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key(
        'post_users_fk', source_table="posts", referent_table="users",
        local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
