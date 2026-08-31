"""create_users_table

Revision ID: b2eb08bef23f
Revises: f924ca1ad734
Create Date: 2026-08-28 09:13:43.065744

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b2eb08bef23f'
down_revision: Union[str, Sequence[str], None] = 'f924ca1ad734'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
