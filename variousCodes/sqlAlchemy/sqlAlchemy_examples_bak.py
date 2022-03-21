import sqlalchemy as sql
from sqlalchemy import create_engine

print(f'SQL Alchemy version: {sql.__version__}')

# ENGINE CREATION IN TO CONNECT TO A DB
engine = create_engine('sqlite:///:memory', echo=True)

