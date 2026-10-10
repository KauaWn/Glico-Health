"""preenche perfil de paciente da Anna

Revision ID: a64b7d9c2e10
Revises: c36005b91f73
Create Date: 2026-10-10

"""
from datetime import date

from alembic import op
import sqlalchemy as sa
from werkzeug.security import generate_password_hash


revision = 'a64b7d9c2e10'
down_revision = 'c36005b91f73'
branch_labels = None
depends_on = None


def upgrade():
    bind = op.get_bind()
    usuario = sa.table(
        'usuario',
        sa.column('id', sa.Integer),
        sa.column('name', sa.String(100)),
        sa.column('username', sa.String(64)),
        sa.column('email', sa.String(64)),
        sa.column('remember_me', sa.Integer),
        sa.column('passw_hash', sa.String(256)),
    )
    paciente = sa.table(
        'paciente',
        sa.column('id', sa.Integer),
        sa.column('id_usuario', sa.Integer),
        sa.column('nascimento', sa.Date),
        sa.column('genero', sa.String(1)),
        sa.column('tipo_diabete', sa.String(20)),
    )
    responsavel = sa.table(
        'responsavel',
        sa.column('id', sa.Integer),
        sa.column('id_usuario', sa.Integer),
        sa.column('responsabilidade', sa.String(30)),
    )
    cuidador = sa.table(
        'cuidador',
        sa.column('id', sa.Integer),
        sa.column('id_usuario', sa.Integer),
        sa.column('tipo_cuidador', sa.String(20)),
    )
    vinculo_responsavel = sa.table(
        'vinculoresponsavel_paciente',
        sa.column('id_responsavel', sa.Integer),
        sa.column('id_paciente', sa.Integer),
    )
    vinculo_cuidador = sa.table(
        'vinculocuidador_paciente',
        sa.column('id_cuidador', sa.Integer),
        sa.column('id_paciente', sa.Integer),
    )
    registro_glicemico = sa.table(
        'registro_glicemico',
        sa.column('id_usuario', sa.Integer),
    )
    evento_calendario = sa.table(
        'evento_calendario',
        sa.column('id_usuario', sa.Integer),
    )

    anna_id = sa.select(usuario.c.id).where(
        usuario.c.username == 'Anna',
        usuario.c.email == 'anna@example.test',
    ).scalar_subquery()

    bind.execute(paciente.update().where(
        paciente.c.id_usuario == anna_id
    ).values(
        nascimento=date(2010, 8, 1),
        genero='F',
        tipo_diabete='tipo1',
    ))

    emails_remover = ('hellen@example.test', 'kaua@example.test')
    ids_remover = sa.select(usuario.c.id).where(usuario.c.email.in_(emails_remover))
    ids_responsaveis = sa.select(responsavel.c.id).where(responsavel.c.id_usuario.in_(ids_remover))
    ids_cuidadores = sa.select(cuidador.c.id).where(cuidador.c.id_usuario.in_(ids_remover))

    bind.execute(vinculo_responsavel.delete().where(
        vinculo_responsavel.c.id_responsavel.in_(ids_responsaveis)
    ))
    bind.execute(vinculo_cuidador.delete().where(
        vinculo_cuidador.c.id_cuidador.in_(ids_cuidadores)
    ))
    bind.execute(registro_glicemico.delete().where(
        registro_glicemico.c.id_usuario.in_(ids_remover)
    ))
    bind.execute(evento_calendario.delete().where(
        evento_calendario.c.id_usuario.in_(ids_remover)
    ))
    bind.execute(responsavel.delete().where(responsavel.c.id_usuario.in_(ids_remover)))
    bind.execute(cuidador.delete().where(cuidador.c.id_usuario.in_(ids_remover)))
    bind.execute(usuario.delete().where(usuario.c.email.in_(emails_remover)))


def downgrade():
    bind = op.get_bind()
    usuario = sa.table(
        'usuario',
        sa.column('id', sa.Integer),
        sa.column('name', sa.String(100)),
        sa.column('username', sa.String(64)),
        sa.column('email', sa.String(64)),
        sa.column('remember_me', sa.Integer),
        sa.column('passw_hash', sa.String(256)),
    )
    paciente = sa.table(
        'paciente',
        sa.column('id', sa.Integer),
        sa.column('id_usuario', sa.Integer),
        sa.column('nascimento', sa.Date),
        sa.column('genero', sa.String(1)),
        sa.column('tipo_diabete', sa.String(20)),
    )
    responsavel = sa.table(
        'responsavel',
        sa.column('id', sa.Integer),
        sa.column('id_usuario', sa.Integer),
        sa.column('responsabilidade', sa.String(30)),
    )
    cuidador = sa.table(
        'cuidador',
        sa.column('id', sa.Integer),
        sa.column('id_usuario', sa.Integer),
        sa.column('tipo_cuidador', sa.String(20)),
    )
    vinculo_responsavel = sa.table(
        'vinculoresponsavel_paciente',
        sa.column('id_responsavel', sa.Integer),
        sa.column('id_paciente', sa.Integer),
        sa.column('relacao', sa.String(30)),
        sa.column('status', sa.String(20)),
        sa.column('criado_por_responsavel', sa.Integer),
        sa.column('data_associacao', sa.DateTime),
    )
    anna_id = sa.select(usuario.c.id).where(
        usuario.c.username == 'Anna',
        usuario.c.email == 'anna@example.test',
    ).scalar_subquery()

    bind.execute(paciente.update().where(
        paciente.c.id_usuario == anna_id,
        paciente.c.nascimento == date(2010, 8, 1),
        paciente.c.genero == 'F',
        paciente.c.tipo_diabete == 'tipo1',
    ).values(
        nascimento=None,
        genero=None,
        tipo_diabete=None,
    ))

    senha_inicial = generate_password_hash('GlicoHealth123!')
    bind.execute(usuario.insert().values(
        name='Hellen',
        username='Hellen',
        remember_me=0,
        email='hellen@example.test',
        passw_hash=senha_inicial,
    ))
    hellen_id = bind.execute(sa.select(usuario.c.id).where(
        usuario.c.email == 'hellen@example.test'
    )).scalar_one()
    bind.execute(usuario.insert().values(
        name='Kaua',
        username='Kaua',
        remember_me=0,
        email='kaua@example.test',
        passw_hash=senha_inicial,
    ))
    kaua_id = bind.execute(sa.select(usuario.c.id).where(
        usuario.c.email == 'kaua@example.test'
    )).scalar_one()
    anna_paciente_id = bind.execute(sa.select(paciente.c.id).where(
        paciente.c.id_usuario == anna_id
    )).scalar_one()
    bind.execute(responsavel.insert().values(
        id_usuario=hellen_id,
        responsabilidade='menor_idade',
    ))
    hellen_responsavel_id = bind.execute(sa.select(responsavel.c.id).where(
        responsavel.c.id_usuario == hellen_id
    )).scalar_one()
    bind.execute(cuidador.insert().values(
        id_usuario=kaua_id,
        tipo_cuidador='profissional',
    ))
    bind.execute(vinculo_responsavel.insert().values(
        id_responsavel=hellen_responsavel_id,
        id_paciente=anna_paciente_id,
        relacao='Mãe',
        status='ativo',
        criado_por_responsavel=0,
        data_associacao=sa.func.now(),
    ))