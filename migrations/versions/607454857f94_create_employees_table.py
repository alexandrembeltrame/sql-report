"""create employees table

Revision ID: 607454857f94
Revises: 
Create Date: 2025-10-27 21:47:22.114161
"""

from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '607454857f94'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create employees table"""
    op.create_table(
        'employees',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('department', sa.String, nullable=False),
        sa.Column('salary', sa.Float, nullable=False),
        sa.Column('performance', sa.Integer, nullable=False)
    )


def downgrade() -> None:
    """Drop employees table"""
    op.drop_table('employees')
