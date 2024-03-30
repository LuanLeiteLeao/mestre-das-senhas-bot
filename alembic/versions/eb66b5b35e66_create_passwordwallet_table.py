"""Create PasswordWallet table

Revision ID: eb66b5b35e66
Revises: 
Create Date: 2024-03-29 21:13:00.366725

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa



# revision identifiers, used by Alembic.
revision: str = 'eb66b5b35e66'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None




# Upgrade operations
def upgrade():
    op.create_table(
        'password_wallet',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True, index=True),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('login', sa.String(), unique=True, nullable=False, index=True),
        sa.Column('password', sa.String(), nullable=True)
    )

# Downgrade operations
def downgrade():
    op.drop_table('password_wallet')

