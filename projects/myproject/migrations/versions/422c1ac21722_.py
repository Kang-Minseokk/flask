"""empty message

Revision ID: 422c1ac21722
Revises: 05b5cecdf502
Create Date: 2023-07-29 16:29:35.607782

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '422c1ac21722'
down_revision = '05b5cecdf502'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###
