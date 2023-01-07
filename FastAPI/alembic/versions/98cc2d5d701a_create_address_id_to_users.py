"""create address_id to users

Revision ID: 98cc2d5d701a
Revises: 2bc4eace1e2c
Create Date: 2023-01-07 20:41:06.782113

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98cc2d5d701a'
down_revision = '2bc4eace1e2c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('users', sa.Column('address_id', sa.Integer(), nullable=True))
    op.create_foreign_key('address_users_fk', source_table='users', referent_table='address',
                          local_cols=['address_id'], remote_cols=["id"], ondelete='CASCADE')

def downgrade() -> None:
    op.drop_constraint('address_users_fk', table_name='users')
    op.drop_column('users', 'address_id')
