import pymysql
import sqlalchemy
from projetoSim.scratches import secrets
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String

engine = sqlalchemy.create_engine(f'mysql+pymysql://root:{secrets.password}@localhost/simChallenge', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Equipe(Base):
    __tablename__ = 'equipes'
    id = Column(Integer, primary_key=True)
    nome_equipe = Column(String(50))

    def __repr__(self):
        return f'ID: {self.id}, Nome da Equipe: {self.nome_equipe}'


Base.metadata.create_all(engine)

equipe = Equipe(nome_equipe='Flamengo')
session.add(equipe)
session.commit()

res = session.query(Equipe).all()
print(res)
session.close()