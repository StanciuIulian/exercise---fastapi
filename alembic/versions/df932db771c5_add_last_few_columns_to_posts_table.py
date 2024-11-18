"""add last few columns to posts table

Revision ID: df932db771c5
Revises: e7752421ef5a
Create Date: 2024-11-17 18:40:39.791805

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'df932db771c5'
down_revision: Union[str, None] = 'e7752421ef5a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', 
                  sa.Column('published', sa.Boolean(), 
                            nullable=False, server_default='TRUE'),)
    op.add_column('posts',
                  sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                            nullable=False, server_default=sa.text('NOW()')),)


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    
