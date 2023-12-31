"""empty message

Revision ID: e5f57a6427af
Revises: 
Create Date: 2023-09-13 03:29:49.995505

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e5f57a6427af'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('advertisement',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=70), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('establishment', sa.Boolean(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_advertisement_id'), 'advertisement', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_advertisement_id'), table_name='advertisement')
    op.drop_table('advertisement')
    # ### end Alembic commands ###
