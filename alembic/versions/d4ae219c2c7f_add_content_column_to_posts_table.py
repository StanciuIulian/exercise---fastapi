"""add content column to posts table

Revision ID: d4ae219c2c7f
Revises: 9a1ebc2e64c8
Create Date: 2024-11-17 17:44:46.283036

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd4ae219c2c7f'
down_revision: Union[str, None] = '9a1ebc2e64c8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'posts',
        sa.Column('cotent', sa.String(), nullable=False)
    )


def downgrade() -> None:
    op.drop_column('posts', 'content')
