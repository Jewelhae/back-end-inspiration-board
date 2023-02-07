"""empty message

Revision ID: fd796d264efd
Revises: 9977e7e3fe04
Create Date: 2023-02-07 10:28:09.057785

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd796d264efd'
down_revision = '9977e7e3fe04'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('board',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=120), nullable=False),
    sa.Column('owner', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('card',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('message', sa.String(), nullable=False),
    sa.Column('likes', sa.Integer(), nullable=False),
    sa.Column('board_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['board_id'], ['board.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('card')
    op.drop_table('board')
    # ### end Alembic commands ###