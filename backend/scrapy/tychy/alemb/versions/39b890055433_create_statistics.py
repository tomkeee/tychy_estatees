"""create Statistics

Revision ID: 39b890055433
Revises: 2cb6f02dcf88
Create Date: 2022-05-21 18:08:07.733357

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '39b890055433'
down_revision = '2cb6f02dcf88'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('flats_statistics',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('flat_number', sa.Integer(), nullable=True),
    sa.Column('flat_average_price', sa.Float(), nullable=True),
    sa.Column('flat_average_rent', sa.Float(), nullable=True),
    sa.Column('flat_m2_average_price', sa.Float(), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('flats_statistics')
    # ### end Alembic commands ###
