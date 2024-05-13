"""create user table

Revision ID: e271f4eaf482
Revises: 
Create Date: 2024-03-18 06:42:45.537251

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e271f4eaf482'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.String(254), primary_key=True),
        sa.Column('email', sa.String(254), nullable=False)
    )


def downgrade():
    op.drop_table('users')
