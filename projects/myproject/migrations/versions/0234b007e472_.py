"""empty message

Revision ID: 0234b007e472
Revises: 597dbda59b83
Create Date: 2023-08-01 14:42:19.850696

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0234b007e472'
down_revision = '597dbda59b83'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('question_voter')
    op.drop_table('answer_voter')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('answer_voter',
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('answer_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['answer_id'], ['answer.id'], name='fk_answer_voter_answer_id_answer', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='fk_answer_voter_user_id_user', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id', 'answer_id', name='pk_answer_voter')
    )
    op.create_table('question_voter',
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('question_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['question.id'], name='fk_question_voter_question_id_question', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='fk_question_voter_user_id_user', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id', 'question_id', name='pk_question_voter')
    )
    # ### end Alembic commands ###
