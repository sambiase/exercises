import sqlalchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

print(f'Versao do sqlAlchemy: {sqlalchemy.__version__}')

# will use sqlite cause it comes with Python but other BDs could be used (postgres, mysql)
# echo=True shows the creation of the table and the codes in SQL

# BD Connection - creation of Engine to connect to the BD
engine = sqlalchemy.create_engine('sqlite:///names.db', echo=True)  # this DB does not exist ate the mo

# Mapping the Object in Python to the one in the BD (ORM)
# needs to import --> from sqlalchemy.orm import declarative_base
Base = declarative_base()


class User(Base):  # class the creates users

    __tablename__ = 'users'  # table Name
    id = Column(Integer, primary_key=True)  # obrigatorio ter um PK
    name = Column(String(50))
    age = Column(Integer)
    cidade = Column(String(30))


# TABLE CREATION IN THE DB
Base.metadata.create_all(engine)  #its after this comand that the DB is created

# CREATING USERS
user = User(name='Andre',age=35,cidade='Rio de Janeiro')

# CREATING A SESSION IN THE DB
# from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

# ADDING OBJECTS IN THE DB IS THE SAME AS "INSERT" FROM SQL
session.add(user)

# NEEDS TO COMMIT IN ORDER TO PERSIST ON THE BD
session.commit()

# ADD MORE USERS
session.add_all([
    User(name='Jose',age=25,cidade='Rio de Janeiro'),
    User(name='Flavia',age=45,cidade='Sao Paulo')])

session.commit()