"""empty message

Revision ID: 5d7c367953eb
Revises: 237df1268348
Create Date: 2021-08-13 15:55:32.331264

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d7c367953eb'
down_revision = '237df1268348'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('articles', 'url',
               existing_type=sa.VARCHAR(length=100),
               type_=sa.String(length=512),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('articles', 'url',
               existing_type=sa.String(length=512),
               type_=sa.VARCHAR(length=100),
               existing_nullable=False)
    # ### end Alembic commands ###
