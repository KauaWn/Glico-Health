"""armazena leituras de temperatura do sensor NTC

Revision ID: d2e3f4a5b6c7
Revises: b7c8d9e0f1a2
Create Date: 2026-10-31

"""
from alembic import op
import sqlalchemy as sa


revision = 'd2e3f4a5b6c7'
down_revision = 'b7c8d9e0f1a2'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'leitura_temperatura',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('temperatura', sa.DECIMAL(precision=5, scale=2), nullable=False),
        sa.Column('data_hora', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_index(
        'ix_leitura_temperatura_data_hora',
        'leitura_temperatura',
        ['data_hora'],
        unique=False,
    )


def downgrade():
    op.drop_index('ix_leitura_temperatura_data_hora', table_name='leitura_temperatura')
    op.drop_table('leitura_temperatura')