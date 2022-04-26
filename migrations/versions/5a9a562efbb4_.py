"""empty message

Revision ID: 5a9a562efbb4
Revises: 1cdd0a5297ca
Create Date: 2022-04-26 17:35:28.785461

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a9a562efbb4'
down_revision = '1cdd0a5297ca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('count_down')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('count_down',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('date', sa.INTEGER(), nullable=True),
    sa.Column('time', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
