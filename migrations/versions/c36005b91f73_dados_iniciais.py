"""dados_iniciais

Revision ID: c36005b91f73
Revises: f0a1b2c3d4e5
Create Date: 2026-10-10 08:20:12.600440

"""
from alembic import op
import sqlalchemy as sa
from werkzeug.security import generate_password_hash


# revision identifiers, used by Alembic.
revision = 'c36005b91f73'
down_revision = 'f0a1b2c3d4e5'
branch_labels = None
depends_on = None


def upgrade():
    bind = op.get_bind()
    metadata = sa.MetaData()
    usuario = sa.Table(
        'usuario', metadata,
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(100)),
        sa.Column('username', sa.String(64)),
        sa.Column('remember_me', sa.Integer),
        sa.Column('email', sa.String(64)),
        sa.Column('passw_hash', sa.String(256)),
    )
    paciente = sa.Table(
        'paciente', metadata,
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('id_usuario', sa.Integer),
    )
    responsavel = sa.Table(
        'responsavel', metadata,
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('id_usuario', sa.Integer),
        sa.Column('responsabilidade', sa.String(30)),
    )
    cuidador = sa.Table(
        'cuidador', metadata,
        sa.Column('id', sa.Integer),
        sa.Column('id_usuario', sa.Integer),
        sa.Column('tipo_cuidador', sa.String(20)),
    )
    vinculo_responsavel_paciente = sa.Table(
        'vinculoresponsavel_paciente', metadata,
        sa.Column('id_responsavel', sa.Integer),
        sa.Column('id_paciente', sa.Integer),
        sa.Column('relacao', sa.String(30)),
        sa.Column('status', sa.String(20)),
        sa.Column('criado_por_responsavel', sa.Integer),
        sa.Column('data_associacao', sa.DateTime),
    )

    senha_inicial = generate_password_hash('GlicoHealth123!')
    anna_id = bind.execute(usuario.insert().values(
        name='Anna',
        username='Anna',
        remember_me=0,
        email='anna@example.test',
        passw_hash=senha_inicial,
    )).inserted_primary_key[0]
    hellen_id = bind.execute(usuario.insert().values(
        name='Hellen',
        username='Hellen',
        remember_me=0,
        email='hellen@example.test',
        passw_hash=senha_inicial,
    )).inserted_primary_key[0]
    kaua_id = bind.execute(usuario.insert().values(
        name='Kaua',
        username='Kaua',
        remember_me=0,
        email='kaua@example.test',
        passw_hash=senha_inicial,
    )).inserted_primary_key[0]

    anna_paciente_id = bind.execute(
        paciente.insert().values(id_usuario=anna_id)
    ).inserted_primary_key[0]
    hellen_responsavel_id = bind.execute(responsavel.insert().values(
        id_usuario=hellen_id,
        responsabilidade='menor_idade',
    )).inserted_primary_key[0]
    bind.execute(cuidador.insert().values(
        id_usuario=kaua_id,
        tipo_cuidador='profissional',
    ))
    bind.execute(vinculo_responsavel_paciente.insert().values(
        id_responsavel=hellen_responsavel_id,
        id_paciente=anna_paciente_id,
        relacao='Mãe',
        status='ativo',
        criado_por_responsavel=0,
        data_associacao=sa.func.now(),
    ))


def downgrade():
    bind = op.get_bind()
    metadata = sa.MetaData()
    usuario = sa.Table(
        'usuario', metadata,
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String(64)),
    )
    paciente = sa.Table(
        'paciente', metadata,
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('id_usuario', sa.Integer),
    )
    responsavel = sa.Table(
        'responsavel', metadata,
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('id_usuario', sa.Integer),
    )
    cuidador = sa.Table(
        'cuidador', metadata,
        sa.Column('id_usuario', sa.Integer),
    )
    vinculo_responsavel_paciente = sa.Table(
        'vinculoresponsavel_paciente', metadata,
        sa.Column('id_responsavel', sa.Integer),
        sa.Column('id_paciente', sa.Integer),
    )

    emails_seed = ('anna@example.test', 'hellen@example.test', 'kaua@example.test')
    ids_usuarios = sa.select(usuario.c.id).where(usuario.c.email.in_(emails_seed))
    ids_pacientes = sa.select(paciente.c.id).where(paciente.c.id_usuario.in_(ids_usuarios))
    ids_responsaveis = sa.select(responsavel.c.id).where(responsavel.c.id_usuario.in_(ids_usuarios))

    bind.execute(vinculo_responsavel_paciente.delete().where(
        vinculo_responsavel_paciente.c.id_responsavel.in_(ids_responsaveis)
    ).where(
        vinculo_responsavel_paciente.c.id_paciente.in_(ids_pacientes)
    ))
    bind.execute(responsavel.delete().where(responsavel.c.id_usuario.in_(ids_usuarios)))
    bind.execute(paciente.delete().where(paciente.c.id_usuario.in_(ids_usuarios)))
    bind.execute(cuidador.delete().where(cuidador.c.id_usuario.in_(ids_usuarios)))
    bind.execute(usuario.delete().where(usuario.c.email.in_(emails_seed)))
