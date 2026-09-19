"""adiciona tipo outro aos eventos do calendario

Revision ID: f0a1b2c3d4e5
Revises: 61b1f13790b8
Create Date: 2026-09-19

"""
from alembic import op
import sqlalchemy as sa


revision = 'f0a1b2c3d4e5'
down_revision = '61b1f13790b8'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('evento_calendario', schema=None) as batch_op:
        batch_op.alter_column(
            'tipo_evento',
            existing_type=sa.Enum(
                'Consulta médica',
                'Exame',
                'Vacina',
                'Registro de glicemia',
                'Tomar medicação',
                name='tipoevento',
            ),
            type_=sa.Enum(
                'Consulta médica',
                'Exame',
                'Vacina',
                'Registro de glicemia',
                'Tomar medicação',
                'Outro',
                name='tipoevento',
            ),
            existing_nullable=True,
        )


def downgrade():
    with op.batch_alter_table('evento_calendario', schema=None) as batch_op:
        batch_op.alter_column(
            'tipo_evento',
            existing_type=sa.Enum(
                'Consulta médica',
                'Exame',
                'Vacina',
                'Registro de glicemia',
                'Tomar medicação',
                'Outro',
                name='tipoevento',
            ),
            type_=sa.Enum(
                'Consulta médica',
                'Exame',
                'Vacina',
                'Registro de glicemia',
                'Tomar medicação',
                name='tipoevento',
            ),
            existing_nullable=True,
        )
