"""ufFf

Revision ID: a635684e82bd
Revises: d8b4a1721529
Create Date: 2024-03-16 01:01:15.083049

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a635684e82bd'
down_revision: Union[str, None] = 'd8b4a1721529'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('donations_gift_id_fkey', 'donations', type_='foreignkey')
    op.drop_column('donations', 'gift_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('donations', sa.Column('gift_id', sa.UUID(), autoincrement=False, nullable=True))
    op.create_foreign_key('donations_gift_id_fkey', 'donations', 'gifts', ['gift_id'], ['uid'])
    # ### end Alembic commands ###
