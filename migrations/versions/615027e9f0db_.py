"""empty message

Revision ID: 615027e9f0db
Revises: f017cfd7a433
Create Date: 2022-04-29 20:46:18.738285

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '615027e9f0db'
down_revision = 'f017cfd7a433'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bookmark', sa.Column('timestamp', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('bookmark', 'timestamp')
    # ### end Alembic commands ###