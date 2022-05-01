"""empty message

Revision ID: 64382429b04a
Revises: 5e4789b5a363
Create Date: 2022-05-01 22:16:48.105398

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64382429b04a'
down_revision = '5e4789b5a363'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    # ### end Alembic commands ###