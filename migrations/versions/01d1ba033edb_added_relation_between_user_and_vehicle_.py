"""Added relation between user and vehicle table, added carrier column which can be null initially

Revision ID: 01d1ba033edb
Revises: 7f8ae8013ec4
Create Date: 2024-09-10 14:04:07.487268

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01d1ba033edb'
down_revision = '7f8ae8013ec4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('carrier', sa.String(length=32), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('carrier')

    # ### end Alembic commands ###
