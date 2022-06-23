"""create posts table

Revision ID: de961299e7f5
Revises: 
Create Date: 2022-06-22 21:21:23.088338

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de961299e7f5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', 
    sa.Column('id', sa.Integer(), nullable = False, primary_key = True),
    sa.Column('title', sa.String(), nullable = False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
