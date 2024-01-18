"""empty message

Revision ID: 5c7310dc1063
Revises: f02cdfa9d016
Create Date: 2024-01-18 20:29:26.928021

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5c7310dc1063'
down_revision: Union[str, None] = 'f02cdfa9d016'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('dish', sa.Column('price', sa.Float(), nullable=False))
    op.add_column('dish', sa.Column('title', sa.String(), nullable=False))
    op.add_column('dish', sa.Column('description', sa.Text(), nullable=False))
    op.drop_column('dish', 'name')
    op.add_column('menu', sa.Column('title', sa.String(), nullable=False))
    op.add_column('menu', sa.Column('description', sa.Text(), nullable=False))
    op.drop_column('menu', 'name')
    op.add_column('submenu', sa.Column('title', sa.String(), nullable=False))
    op.add_column('submenu', sa.Column('description', sa.Text(), nullable=False))
    op.alter_column('submenu', 'menu_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('submenu', 'name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('submenu', sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.alter_column('submenu', 'menu_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_column('submenu', 'description')
    op.drop_column('submenu', 'title')
    op.add_column('menu', sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('menu', 'description')
    op.drop_column('menu', 'title')
    op.add_column('dish', sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('dish', 'description')
    op.drop_column('dish', 'title')
    op.drop_column('dish', 'price')
    # ### end Alembic commands ###