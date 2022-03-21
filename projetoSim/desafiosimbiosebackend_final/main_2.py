import json

from flask import Flask, jsonify, request
import pymysql
import sqlalchemy
from projetoSim.scratches import secrets
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String

app = Flask(__name__)

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


@app.route('/teams', methods=['POST'])
def register_teams():
    # Get data from the POST body
    request_data = request.get_json()
    teams = Team(team_name=request_data["teamname"])
    session.add(teams)
    session.commit()
    return jsonify(request_data)


@app.route('/employees', methods=['POST'])
def register_employees():
    # Get data from the POST body
    request_data = request.get_json()

    return_dict = {"example": "Register employees!"}

    return jsonify(return_dict)


@app.route('/recommendations', methods=['POST'])
def register_recommendations():
    # Get data from the POST body
    request_data = request.get_json()

    return_dict = {"example": "Register recommendations!"}

    return jsonify(return_dict)


@app.route('/teams', methods=['GET'])
def get_all_teams():
    res = session.query(Team).all()
    print(res)
    session.close()

    return_dict = json.dumps(res)

    return jsonify(return_dict)


@app.route('/recommendations', methods=['GET'])
def get_all_recommendations():
    return_dict = {"example": "List recommendations!"}

    return jsonify(return_dict)


@app.route('/recommendations/employees', methods=['GET'])
def get_all_employees_with_recommendations():
    return_dict = {"example": "List employees!"}

    return jsonify(return_dict)


if __name__ == "__main__":
    app.run(debug=True)
