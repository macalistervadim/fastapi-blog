"""add nullable to column

Revision ID: 49e7c682482a
Revises: 42312596f37c
Create Date: 2025-04-23 17:02:36.592107

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '49e7c682482a'
down_revision: Union[str, None] = '42312596f37c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
