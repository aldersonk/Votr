"""empty message

Revision ID: 23e40b9b14f9
Revises: 3c373ee3a69a
Create Date: 2017-01-04 23:59:20.824679

"""

# revision identifiers, used by Alembic.
revision = '23e40b9b14f9'
down_revision = '3c373ee3a69a'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('topics', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_identifier', sa.String(length=100), nullable=True))

    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('topics', schema=None) as batch_op:
        batch_op.drop_column('user_identifier')

    ### end Alembic commands ###