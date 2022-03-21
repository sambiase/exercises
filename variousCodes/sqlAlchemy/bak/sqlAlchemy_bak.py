import sqlalchemy
from sqlalchemy.orm import declarative_base, session
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

print(f'Versao do sqlAlchemy: {sqlalchemy.__version__}')

# will use sqlite cause it comes with Python but other BDs could be used (postgres, mysql)
# echo=True shows the creation of the table and the codes in SQL

# BD Connection - creation of Engine to connect to the BD
engine = sqlalchemy.create_engine('sqlite:///names.db', echo=True)  # this DB does not exist ate the mo


# CREATING A SESSION IN THE DB (from sqlalchemy.orm import sessionmaker)
Session = sessionmaker(bind=engine)
session = Session()


# MAPPING the Object in Python to the one in the BD (ORM)
# needs to import --> from sqlalchemy.orm import declarative_base
Base = declarative_base()


# CLASS TO CREATE USERS and TO DEFINE TABLE PROPERTIES
# ESTA CLASSE HERDA DE BASE QUE EH A CLASSE BASE DO SQLALCHEMY
class User(Base):
    __tablename__ = 'users'  # TABLE NAME

    id = Column(Integer, primary_key=True)  # obrigatório ter um PK
    name = Column(String(50))
    age = Column(Integer)
    cidade = Column(String(30))

    # funcao usada para retornar os valores quando fizermos uma QUERY na tabela
    def __repr__(self):
        return f'Id: {self.id}, Nome: {self.name}, Idade: {self.age}, Cidade: {self.cidade}'


# TABLE CREATION IN THE DB
Base.metadata.create_all(engine)  # its after this command that the DB is actually created

# CREATING USERS
user = User(name='Andre', age=35, cidade='Rio de Janeiro')

# ADDING OBJECTS = "INSERT" DO SQL
session.add(user)

# NEEDS TO COMMIT IN ORDER TO PERSIST ON THE BD
session.commit()

# ADD MORE USERS AT ONCE
session.add_all([
    User(name='Jose', age=25, cidade='Rio de Janeiro'),
    User(name='Flavia', age=45, cidade='Sao Paulo')])

# session.commit()

# CONSULTAR O DB = "SELECT" DO SQL
res_one_user = session.query(User).filter_by(name='Andre')
first_user = session.query(User).first()  # retorna o primeiro registro no BD
getPrimaryKey = session.query(User).get(1)
all_users = session.query(User.id,User.name).all()
filter_ID = session.query(User).filter(User.id==2)
user1 = session.query(User).filter(User.id==1).first()
user2 = session.query(User).filter(User.id==1).first()

print(f'{user1 is user2}')

print(f'\nFirst user added in the DB: {first_user}')
print(f'Primary Key ID 1: {getPrimaryKey}')
print(f'All Users: {all_users}')
print(f'Filtrar por Rio de Janeiro: {filter_ID}')




session.close()
'''
for all_users in session.query(User).order_by(User.id):
    print(all_users.name)

# CHANGE OBJECTS = "UPDATE" DO SQL
user.name = 'Flamengo'
session.commit()

# DELETE AN OBJECT = "DELETE" NO SQL
# user = session.query(User).filter_by(name='Flamengo')
# session.delete(user)
'''
