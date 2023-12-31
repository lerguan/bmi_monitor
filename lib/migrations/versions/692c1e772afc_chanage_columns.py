"""chanage columns

Revision ID: 692c1e772afc
Revises: a37dd2e3cb69
Create Date: 2023-08-25 23:34:45.944899

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '692c1e772afc'
down_revision: Union[str, None] = 'a37dd2e3cb69'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bmis', sa.Column('age', sa.Integer(), nullable=True))
    op.drop_column('bmis', 'date')
    op.drop_column('users', 'age')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('age', sa.INTEGER(), nullable=True))
    op.add_column('bmis', sa.Column('date', sa.DATETIME(), nullable=True))
    op.drop_column('bmis', 'age')
    # ### end Alembic commands ###
