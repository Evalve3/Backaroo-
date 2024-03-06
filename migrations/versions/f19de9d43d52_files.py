"""files

Revision ID: f19de9d43d52
Revises: 6ecdd713dade
Create Date: 2024-03-06 22:07:08.446770

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f19de9d43d52'
down_revision: Union[str, None] = '6ecdd713dade'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('files',
    sa.Column('uid', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('data', sa.LargeBinary(), nullable=False),
    sa.PrimaryKeyConstraint('uid')
    )
    op.add_column('collects', sa.Column('image_id', sa.UUID(), nullable=True))
    op.create_foreign_key(None, 'collects', 'files', ['image_id'], ['uid'])
    op.add_column('users', sa.Column('avatar_id', sa.UUID(), nullable=True))
    op.create_foreign_key(None, 'users', 'files', ['avatar_id'], ['uid'])
    op.drop_column('users', 'profile_background')
    op.drop_column('users', 'avatar')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('avatar', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('profile_background', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'avatar_id')
    op.drop_constraint(None, 'collects', type_='foreignkey')
    op.drop_column('collects', 'image_id')
    op.drop_table('files')
    # ### end Alembic commands ###
