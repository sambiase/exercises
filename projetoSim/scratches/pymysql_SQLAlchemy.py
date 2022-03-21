import pymysql
import sqlalchemy
from projetoSim.scratches import secrets
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String

engine = sqlalchemy.create_engine(f'mysql+pymysql://root:{secrets.password}@localhost/simChallenge', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Team(Base):
    __tablename__ = 'teams'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    team_name = Column(String(50))

    def __repr__(self):
        return f'ID: {self.id}, Nome da Equipe: {self.team_name}'


Base.metadata.create_all(engine)

team = Team(team_name='Flamengo')
session.add(team)
session.commit()

res = session.query(Team).all()
print(res)
session.close()
