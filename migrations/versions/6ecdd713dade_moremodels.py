"""moreModels

Revision ID: 6ecdd713dade
Revises: d60b344dd997
Create Date: 2024-03-06 01:29:42.176888

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6ecdd713dade'
down_revision: Union[str, None] = 'd60b344dd997'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('uid', sa.UUID(), nullable=False),
    sa.Column('author_id', sa.UUID(), nullable=False),
    sa.Column('text', sa.String(), nullable=False),
    sa.Column('create_date', sa.Date(), server_default=sa.text('now()'), nullable=False),
    sa.Column('collect_id', sa.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['users.uid'], ),
    sa.ForeignKeyConstraint(['collect_id'], ['collects.uid'], ),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('news',
    sa.Column('uid', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('text', sa.String(), nullable=False),
    sa.Column('create_date', sa.Date(), server_default=sa.text('now()'), nullable=False),
    sa.Column('collect_id', sa.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['collect_id'], ['collects.uid'], ),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('questions',
    sa.Column('uid', sa.UUID(), nullable=False),
    sa.Column('text', sa.String(), nullable=False),
    sa.Column('collect_id', sa.UUID(), nullable=False),
    sa.Column('author_id', sa.UUID(), nullable=False),
    sa.Column('create_date', sa.Date(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['users.uid'], ),
    sa.ForeignKeyConstraint(['collect_id'], ['collects.uid'], ),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('subscribe_notifications',
    sa.Column('uid', sa.UUID(), nullable=False),
    sa.Column('collect_id', sa.UUID(), nullable=False),
    sa.Column('user_id', sa.UUID(), nullable=False),
    sa.Column('create_date', sa.Date(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['collect_id'], ['collects.uid'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.uid'], ),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('support_question',
    sa.Column('uid', sa.UUID(), nullable=False),
    sa.Column('author_id', sa.UUID(), nullable=False),
    sa.Column('create_date', sa.Date(), server_default=sa.text('now()'), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.Column('category_id', sa.UUID(), nullable=False),
    sa.Column('collect_id', sa.UUID(), nullable=False),
    sa.Column('text', sa.String(), nullable=False),
    sa.Column('need_answer', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['users.uid'], ),
    sa.ForeignKeyConstraint(['category_id'], ['support_categories.uid'], ),
    sa.ForeignKeyConstraint(['collect_id'], ['collects.uid'], ),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('notifications',
    sa.Column('uid', sa.UUID(), nullable=False),
    sa.Column('subscribe_id', sa.UUID(), nullable=False),
    sa.Column('text', sa.Text(), nullable=False),
    sa.Column('create_date', sa.Date(), server_default=sa.text('now()'), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['subscribe_id'], ['subscribe_notifications.uid'], ),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('question_answers',
    sa.Column('uid', sa.UUID(), nullable=False),
    sa.Column('question_id', sa.UUID(), nullable=False),
    sa.Column('author_id', sa.UUID(), nullable=False),
    sa.Column('text', sa.String(), nullable=False),
    sa.Column('create_date', sa.Date(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['users.uid'], ),
    sa.ForeignKeyConstraint(['question_id'], ['questions.uid'], ),
    sa.PrimaryKeyConstraint('uid')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('question_answers')
    op.drop_table('notifications')
    op.drop_table('support_question')
    op.drop_table('subscribe_notifications')
    op.drop_table('questions')
    op.drop_table('news')
    op.drop_table('comments')
    # ### end Alembic commands ###
