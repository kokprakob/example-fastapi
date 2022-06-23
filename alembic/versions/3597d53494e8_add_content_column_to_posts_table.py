"""add content column to posts table

Revision ID: 3597d53494e8
Revises: de961299e7f5
Create Date: 2022-06-22 21:27:21.817939

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3597d53494e8'
down_revision = 'de961299e7f5'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',
    sa.Column('content', sa.String(), nullable = False)
    )
    pass

def downgrade():
    op.drop_column('posts', 'content')
    pass