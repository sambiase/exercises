import json
import sqlalchemy

from flask import Flask, jsonify, request
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from projetoSim.scratches import secrets
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String

app = Flask(__name__)

engine = sqlalchemy.create_engine(f'mysql+pymysql://root:{secrets.password}@localhost/simChallenge', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Table Creation on MySql
class Team(Base):
    __tablename__ = 'teams'

    id = Column(Integer, primary_key=True, nullable=False)
    team_name = Column(String(50))

    def __repr__(self):
        return f'ID: {self.id}, Team Name: {self.team_name}'


# Table Creation on MySql
class Recommendation(Base):
    __tablename__ = 'recommendations'

    id = Column(Integer, primary_key=True, nullable=False)
    recommendations = Column(String(50))

    def __repr__(self):
        return f'ID: {self.id}, Recommendations: {self.recommendations}'


Base.metadata.create_all(engine)
ma = Marshmallow(app)


class TeamSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Team


@app.route('/teams', methods=['POST'])
def register_teams():
    # data gotten from POST BODY Json - Postman
    request_data = request.get_json()

    # check if team name exists
    if "team_name" not in request_data:
        return {"status": 400, "message": "ID and Team Name are mandatory fields"}
    else:
        teams = Team(id=request_data["id"], team_name=request_data["team_name"])

        # INSERT data to MySql Table
        session.add(teams)
        session.commit()

        # return posted on Postman
        return jsonify(request_data)


@app.route('/employees', methods=['POST'])
def register_employees():
    # data gotten from POST BODY Json - Postman
    request_data = request.get_json()

    return_dict = {"example": "Register employees!"}

    return jsonify(return_dict)


@app.route('/recommendations', methods=['POST'])
def register_recommendations():
    # data gotten from POST BODY Json - Postman
    request_data = request.get_json()

    if "recommendations" not in request_data:
        return {"status": 400, "recommendations": "Recommendation is a mandatory field"}
    else:
        recommendations = Recommendation(id=request_data["id"], recommendations=request_data["recommendations"])

        # INSERT data to MySql Table
        session.add(recommendations)
        session.commit()

        # return on Postman
        return jsonify(request_data)


@app.route('/teams', methods=['GET'])
def get_all_teams():
    res = session.query(Team).all()
    team_schema = TeamSchema()
    res_json = team_schema.dump(res, many=True)
    return jsonify(res_json)


@app.route('/recommendations', methods=['GET'])
def get_all_recommendations():
    res = session.query(Recommendation).all()

    # print(resJson)

    return jsonify(json.dumps([dict(r) for r in res]))


@app.route('/recommendations/employees', methods=['GET'])
def get_all_employees_with_recommendations():
    return_dict = {"example": "List employees!"}

    return jsonify(return_dict)


if __name__ == "__main__":
    app.run(debug=True)
