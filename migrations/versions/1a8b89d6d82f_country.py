"""country

Revision ID: 1a8b89d6d82f
Revises: f19de9d43d52
Create Date: 2024-03-08 03:03:33.984127

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1a8b89d6d82f'
down_revision: Union[str, None] = 'f19de9d43d52'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('countries', 'icon_url')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('countries', sa.Column('icon_url', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###