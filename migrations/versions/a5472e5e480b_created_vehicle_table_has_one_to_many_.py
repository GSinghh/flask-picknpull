"""Created vehicle table. Has one to many relation with user

Revision ID: a5472e5e480b
Revises: 01d1ba033edb
Create Date: 2024-09-10 14:35:31.080637

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a5472e5e480b'
down_revision = '01d1ba033edb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vehicles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start_year', sa.String(length=16), nullable=True),
    sa.Column('end_year', sa.String(length=16), nullable=True),
    sa.Column('postal_code', sa.String(length=16), nullable=False),
    sa.Column('distance', sa.String(length=16), nullable=False),
    sa.Column('make', sa.String(length=16), nullable=False),
    sa.Column('model', sa.String(length=16), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vehicles')
    # ### end Alembic commands ###