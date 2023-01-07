"""create phone number for user col

Revision ID: 5db9f2714784
Revises: 
Create Date: 2023-01-07 20:00:28.829659

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5db9f2714784'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("users", sa.Column("phone_number", sa.String(32), nullable=True))


def downgrade() -> None:
    op.drop_column('users', 'phone_number')
    
