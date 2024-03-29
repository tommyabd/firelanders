"""empty message

Revision ID: 15605937f80e
Revises: 
Create Date: 2022-04-12 16:23:29.305534

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15605937f80e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('slide_show',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('file', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('slide_show')
    # ### end Alembic commands ###
