from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import csv
from datetime import datetime
from sqlalchemy.exc import IntegrityError

Base = declarative_base()

class Municipio(Base):
    __tablename__ = 'municipios'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), unique=True, nullable=False)
    
    registros = relationship("RegistroDengue", back_populates="municipio")

class Superintendencia(Base):
    __tablename__ = 'superintendencias'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), unique=True, nullable=False)
    
    registros = relationship("RegistroDengue", back_populates="superintendencia")

class ADS(Base):
    __tablename__ = 'ads'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), unique=True, nullable=False)
    
    registros = relationship("RegistroDengue", back_populates="ads")

class RegistroDengue(Base):
    __tablename__ = 'registros_dengue'
    
    id = Column(Integer, primary_key=True)
    ano = Column(Integer, nullable=False)
    tipo_arbovirose = Column(String(50), nullable=False)
    data_epidemiologica = Column(Date, nullable=False)
    semana_epidemiologica = Column(Integer, nullable=False)
    dengue_grave = Column(Integer, default=0)
    cura = Column(Integer, default=0)
    obito = Column(Integer, default=0)
    obito_investigacao = Column(Integer, default=0)
    confirmado_ambulatorial = Column(Integer, default=0)
    confirmado_clinico = Column(Integer, default=0)
    
    # Relacionamentos
    municipio_id = Column(Integer, ForeignKey('municipios.id'))
    municipio = relationship("Municipio", back_populates="registros")
    
    superintendencia_id = Column(Integer, ForeignKey('superintendencias.id'))
    superintendencia = relationship("Superintendencia", back_populates="registros")
    
    ads_id = Column(Integer, ForeignKey('ads.id'))
    ads = relationship("ADS", back_populates="registros")


engine = create_engine('sqlite:///dengue.db')  
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def carregar_dados(caminho_arquivo):
    with open(caminho_arquivo, mode='r', encoding='latin1') as arquivo:
        leitor = csv.DictReader(arquivo, delimiter=';')
        
        for linha in leitor:
            # Tratar dados (remover aspas se necessário)
            dados = {k.strip('"'): v.strip('"') for k, v in linha.items()}
            
            # Verificar/inserir município
            municipio = session.query(Municipio).filter_by(nome=dados['MUNICÍPIO']).first()
            if not municipio:
                municipio = Municipio(nome=dados['MUNICÍPIO'])
                session.add(municipio)
                session.commit()
            
            # Verificar/inserir superintendência
            superintendencia = session.query(Superintendencia).filter_by(nome=dados['SUPERINTENDENCIA']).first()
            if not superintendencia:
                superintendencia = Superintendencia(nome=dados['SUPERINTENDENCIA'])
                session.add(superintendencia)
                session.commit()
            
            # Verificar/inserir ADS
            ads = session.query(ADS).filter_by(nome=dados['ADS']).first()
            if not ads:
                ads = ADS(nome=dados['ADS'])
                session.add(ads)
                session.commit()
            
            # Converter data
            data_epid = datetime.strptime(dados['DATA_EPIDEMIOLOGICA'], '%Y-%m-%d').date()
            
            # Criar registro de dengue
            registro = RegistroDengue(
                ano=int(dados['ANO']),
                tipo_arbovirose=dados['TIPO_ABOVIROSE'],
                data_epidemiologica=data_epid,
                semana_epidemiologica=int(dados['SEMANA_EPIDEMIOLOGICA']),
                dengue_grave=int(dados['DENGUE_GRAVE']),
                cura=int(dados['CURA']),
                obito=int(dados['OBITO']),
                obito_investigacao=int(dados['OBITO_INVESTIGACAO']),
                confirmado_ambulatorial=int(dados['CONFIRMADO_AMBULATORIAL']),
                confirmado_clinico=int(dados['CONFIRMADO_CLINICO']),
                municipio_id=municipio.id,
                superintendencia_id=superintendencia.id,
                ads_id=ads.id
            )
            
            session.add(registro)
        
        try:
            session.commit()
        except IntegrityError:
            session.rollback()
            print("Erro ao inserir dados. Verifique possíveis duplicatas.")
        except Exception as e:
            session.rollback()
            print(f"Erro inesperado: {str(e)}")

# Uso
carregar_dados('cenario_arbovirose_2025-05-04_13-03-34.csv')
#df = pd.read_csv("cenario_arbovirose_2025-05-04_13-03-34.csv", encoding='latin1', sep=';', quotechar='"')