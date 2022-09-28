"""empty message

Revision ID: 90063792a995
Revises: 5d7c367953eb
Create Date: 2022-07-19 19:44:43.086027

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '90063792a995'
down_revision = '5d7c367953eb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('articles', sa.Column('article_editor', sa.String(length=100), nullable=True))
    op.alter_column('articles', 'url',
               existing_type=mysql.VARCHAR(length=512),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('articles', 'url',
               existing_type=mysql.VARCHAR(length=512),
               nullable=False)
    op.drop_column('articles', 'article_editor')
    # ### end Alembic commands ###
