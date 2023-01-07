"""Create address tab

Revision ID: 80accd336197
Revises: 5db9f2714784
Create Date: 2023-01-07 20:19:30.955042

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80accd336197'
down_revision = '5db9f2714784'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('address',
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('address1', sa.String(16), nullable=False),
                    sa.Column('address2', sa.String(16), nullable=False),
                    sa.Column('city', sa.String(16), nullable=False),
                    sa.Column('state', sa.String(16), nullable=False),
                    sa.Column('country', sa.String(16), nullable=False),
                    sa.Column('postalcode', sa.String(16), nullable=False))


def downgrade() -> None:
    op.drop_table('address')
