"""empty message

Revision ID: 5fa4dfd706f4
Revises: 9896d5181424
Create Date: 2022-04-19 21:55:18.610966

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5fa4dfd706f4'
down_revision = '9896d5181424'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contact_us',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('lastname', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('number', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_column('contact', 'name')
    op.drop_column('contact', 'lastname')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contact', sa.Column('lastname', sa.VARCHAR(), nullable=True))
    op.add_column('contact', sa.Column('name', sa.VARCHAR(), nullable=True))
    op.drop_table('contact_us')
    # ### end Alembic commands ###
