from typing import Optional
import datetime
import enum

from sqlalchemy import CHAR, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, String, text
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass


class CuidadorTipoCuidador(str, enum.Enum):
    FAMILIAR = 'familiar'
    PROFISSIONAL = 'profissional'


class PacienteTipoDiabete(str, enum.Enum):
    TIPO1 = 'tipo1'
    TIPO2 = 'tipo2'
    GESTACIONAL = 'gestacional'


class VinculoresponsavelPacienteStatus(str, enum.Enum):
    ATIVO = 'ativo'
    DESATIVADO = 'desativado'
    PENDENTE = 'pendente'


class Usuario(Base):
    __tablename__ = 'usuario'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    username: Mapped[str] = mapped_column(String(64), nullable=False)
    remember_me: Mapped[int] = mapped_column(TINYINT, nullable=False)
    email: Mapped[Optional[str]] = mapped_column(String(64))
    passw_hash: Mapped[Optional[str]] = mapped_column(String(256))

    cuidador: Mapped[list['Cuidador']] = relationship('Cuidador', back_populates='usuario')
    paciente: Mapped[list['Paciente']] = relationship('Paciente', back_populates='usuario')
    responsavel: Mapped[list['Responsavel']] = relationship('Responsavel', back_populates='usuario')


class Cuidador(Base):
    __tablename__ = 'cuidador'
    __table_args__ = (
        ForeignKeyConstraint(['id_usuario'], ['usuario.id'], name='fk_usuario_cuidador'),
        Index('fk_usuario_cuidador_idx', 'id_usuario')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    id_usuario: Mapped[int] = mapped_column(Integer, primary_key=True)
    tipo_cuidador: Mapped[Optional[CuidadorTipoCuidador]] = mapped_column(Enum(CuidadorTipoCuidador, values_callable=lambda cls: [member.value for member in cls]))
    conselho_profissional: Mapped[Optional[str]] = mapped_column(String(10))
    registro_profissional: Mapped[Optional[str]] = mapped_column(String(20))

    usuario: Mapped['Usuario'] = relationship('Usuario', back_populates='cuidador')
    vinculocuidador_paciente: Mapped[list['VinculocuidadorPaciente']] = relationship('VinculocuidadorPaciente', back_populates='cuidador')


class Paciente(Base):
    __tablename__ = 'paciente'
    __table_args__ = (
        ForeignKeyConstraint(['id_usuario'], ['usuario.id'], name='fk_usuario_paciente'),
        Index('fk_usuario_paciente_idx', 'id_usuario')
    )

    id: Mapped[int] = mapped_column(Integer,primary_key=True,autoincrement=True)
    id_usuario: Mapped[int] = mapped_column(Integer,nullable=False)
    nascimento: Mapped[Optional[datetime.date]] = mapped_column(Date)
    genero: Mapped[Optional[str]] = mapped_column(CHAR(1))
    tipo_diabete: Mapped[Optional[PacienteTipoDiabete]] = mapped_column(Enum(PacienteTipoDiabete, values_callable=lambda cls: [member.value for member in cls]))

    usuario: Mapped['Usuario'] = relationship('Usuario', back_populates='paciente')
    vinculocuidador_paciente: Mapped[list['VinculocuidadorPaciente']] = relationship('VinculocuidadorPaciente', back_populates='paciente')
    vinculoresponsavel_paciente: Mapped[list['VinculoresponsavelPaciente']] = relationship('VinculoresponsavelPaciente', back_populates='paciente')


class Responsavel(Base):
    __tablename__ = 'responsavel'
    __table_args__ = (
        ForeignKeyConstraint(['id_usuario'], ['usuario.id'], name='fk_usuario_responsavel'),
        Index('fk_usuario_responsavel_idx', 'id_usuario')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    id_usuario: Mapped[int] = mapped_column(Integer, primary_key=True)
    responsabilidade: Mapped[Optional[str]] = mapped_column(String(30))

    usuario: Mapped['Usuario'] = relationship('Usuario', back_populates='responsavel')
    vinculoresponsavel_paciente: Mapped[list['VinculoresponsavelPaciente']] = relationship('VinculoresponsavelPaciente', back_populates='responsavel')


class VinculocuidadorPaciente(Base):
    __tablename__ = 'vinculocuidador_paciente'
    __table_args__ = (
        ForeignKeyConstraint(['id_cuidador'], ['cuidador.id'], name='fk_cuidador_vinculo'),
        ForeignKeyConstraint(['id_paciente'], ['paciente.id'], name='fk_cuidador_paciente'),
        Index('fk_cuidador_paciente_idx', 'id_paciente')
    )

    id_cuidador: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_paciente: Mapped[int] = mapped_column(Integer, primary_key=True)
    criado_por_cuidador: Mapped[int] = mapped_column(TINYINT, nullable=False, server_default=text("'0'"))
    data_associacao: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False)
    status: Mapped[Optional[str]] = mapped_column(String(20), server_default=text("'Pendente'"))

    cuidador: Mapped['Cuidador'] = relationship('Cuidador', back_populates='vinculocuidador_paciente')
    paciente: Mapped['Paciente'] = relationship('Paciente', back_populates='vinculocuidador_paciente')


class VinculoresponsavelPaciente(Base):
    __tablename__ = 'vinculoresponsavel_paciente'
    __table_args__ = (
        ForeignKeyConstraint(['id_paciente'], ['paciente.id'], name='fk_paciente_responsavel'),
        ForeignKeyConstraint(['id_responsavel'], ['responsavel.id'], name='fk_responsavel_vinculo'),
        Index('fk_paciente_responsavel_idx', 'id_paciente')
    )

    id_responsavel: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_paciente: Mapped[int] = mapped_column(Integer, primary_key=True)
    relacao: Mapped[Optional[str]] = mapped_column(String(30))
    status: Mapped[Optional[VinculoresponsavelPacienteStatus]] = mapped_column(Enum(VinculoresponsavelPacienteStatus, values_callable=lambda cls: [member.value for member in cls]))
    criado_por_responsavel: Mapped[Optional[int]] = mapped_column(TINYINT, server_default=text("'0'"))
    data_associacao: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)

    paciente: Mapped['Paciente'] = relationship('Paciente', back_populates='vinculoresponsavel_paciente')
    responsavel: Mapped['Responsavel'] = relationship('Responsavel', back_populates='vinculoresponsavel_paciente')
