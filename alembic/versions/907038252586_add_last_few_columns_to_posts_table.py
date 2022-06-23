"""add last few columns to posts table

Revision ID: 907038252586
Revises: f6d4ec83612a
Create Date: 2022-06-22 22:19:03.214930

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '907038252586'
down_revision = 'f6d4ec83612a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), server_default= 'TRUE'))
    op.add_column('posts', sa.Column('created_as', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()'))
         
    )
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_as')
    pass
