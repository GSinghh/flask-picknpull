"""Created results table with one to one relationship with vehicle table

Revision ID: 1e51bf029b1a
Revises: a5472e5e480b
Create Date: 2024-09-10 17:55:41.195627

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e51bf029b1a'
down_revision = 'a5472e5e480b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('results',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('year', sa.String(), nullable=False),
    sa.Column('model', sa.String(), nullable=False),
    sa.Column('make', sa.String(), nullable=False),
    sa.Column('row', sa.String(), nullable=False),
    sa.Column('image_url', sa.String(), nullable=False),
    sa.Column('date_added', sa.String(), nullable=False),
    sa.Column('vehicle_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['vehicle_id'], ['vehicles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('vehicles', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['user_id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vehicles', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    op.drop_table('results')
    # ### end Alembic commands ###
