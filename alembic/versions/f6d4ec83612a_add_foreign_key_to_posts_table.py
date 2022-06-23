"""add foreign_key to posts table

Revision ID: f6d4ec83612a
Revises: 75e79b302115
Create Date: 2022-06-22 21:39:16.517006

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f6d4ec83612a'
down_revision = '75e79b302115'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table = "posts", referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
     
    pass

def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass