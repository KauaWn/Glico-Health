"""garante e-mail único por usuário

Revision ID: b7c8d9e0f1a2
Revises: a64b7d9c2e10
Create Date: 2026-10-27

"""
from alembic import op
import sqlalchemy as sa


revision = "b7c8d9e0f1a2"
down_revision = "a64b7d9c2e10"
branch_labels = None
depends_on = None


def upgrade():
    bind = op.get_bind()
    usuario = sa.table(
        "usuario",
        sa.column("id", sa.Integer),
        sa.column("email", sa.String(64)),
    )
    email_normalizado = sa.func.lower(sa.func.trim(usuario.c.email))
    emails_duplicados = bind.execute(
        sa.select(email_normalizado)
        .where(usuario.c.email.is_not(None), sa.func.trim(usuario.c.email) != "")
        .group_by(email_normalizado)
        .having(sa.func.count(usuario.c.id) > 1)
    ).scalars().all()

    for email in emails_duplicados:
        ids = bind.execute(
            sa.select(usuario.c.id)
            .where(email_normalizado == email)
            .order_by(usuario.c.id)
        ).scalars().all()
        bind.execute(
            usuario.update()
            .where(usuario.c.id.in_(ids[1:]))
            .values(email=None)
        )

    op.create_index("uq_usuario_email", "usuario", ["email"], unique=True)


def downgrade():
    op.drop_index("uq_usuario_email", table_name="usuario")