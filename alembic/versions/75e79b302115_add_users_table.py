"""add users table

Revision ID: 75e79b302115
Revises: 3597d53494e8
Create Date: 2022-06-22 21:33:14.614262

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75e79b302115'
down_revision = '3597d53494e8'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users', 
    sa.Column('id', sa.Integer(), primary_key= True, nullable= False, index=True),
    sa.Column('email', sa.String(), nullable=False, unique=True),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('created_as', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    pass


def downgrade():
    op.drop_table('users')
    pass
