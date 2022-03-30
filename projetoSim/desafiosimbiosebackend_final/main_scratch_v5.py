import json
import sqlalchemy

from flask import Flask, jsonify, request
from flask_marshmallow import Marshmallow, fields

from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from projetoSim.scratches import secrets
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

app = Flask(__name__)

engine = sqlalchemy.create_engine(f'mysql+pymysql://root:{secrets.password}@localhost/simChallenge', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
ma = Marshmallow(app)


# TABLE CREATION ON MYSQL - FUNCIONARIOS
class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True, nullable=False)
    employee_name = Column(String(50))

    team_id = Column(Integer, ForeignKey('teams.id'), nullable=False)
    teams = relationship('Team', back_populates='employees')

    def __repr__(self) -> str:
        return f'ID: {self.id} , Employee Name: {self.employee_name}'


# TABLE CREATION ON MYSQL - EQUIPE
class Team(Base):
    __tablename__ = 'teams'

    id = Column(Integer, primary_key=True, nullable=False)
    team_name = Column(String(50), nullable=False)

    employees = relationship('Employee', back_populates='teams')  # Employee --> references Class Employee / backref references

    def __repr__(self) -> str:
        return f'ID: {self.id}, Team Name: {self.team_name}, Employees: {self.employees}'


# TABLE CREATION ON MYSQL - INDICACOES
class Recommendation(Base):
    __tablename__ = 'recommendations'

    id = Column(Integer, primary_key=True, nullable=False)
    recommendation = Column(String(50))


Base.metadata.create_all(engine)


# SERIALIZED TABLE "TEAM" SCHEMA
class TeamSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Team
        fields = ('id','team_name')


class EmployeeTeamSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Employee
        fields = ('id','employee_name','team')



# SERIALIZED TABLE "RECOMMENDATION" SCHEMA
class RecoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Recommendation


@app.route('/teams', methods=['POST'])  # Registrar Equipes(times) - OK
def register_teams():
    # DATA GOTTEN FROM POST BODY JSON - POSTMAN
    request_data = request.get_json()

    # CHECK IF TEAM NAME EXISTS
    if "team_name" not in request_data:
        return {"status": 400, "message": "ID and Team Name are mandatory fields"}
    else:
        teams = Team(id=request_data["id"], team_name=request_data["team_name"])

        # INSERT DATA TO MYSQL TABLE
        session.add(teams)
        session.commit()

        # RETURN POST ON POSTMAN
        return jsonify(request_data)


@app.route('/employees', methods=['POST'])  # Registrar Funcionarios - OK
def register_employees():
    # DATA GOTTEN FROM POST BODY JSON - POSTMAN
    request_data = request.get_json()
    print('REQUEST:', request_data)
    # CHECK IF EMPLOYEE NAME EXISTS
    if "employee_name" not in request_data:
        return {"status": 400, "message": "Employee Name is a mandatory field"}
    else:
        employee = Employee(id=request_data["id"], employee_name=request_data["employee_name"],
                            team_id=request_data["team_id"])

        # INSERT DATA TO MYSQL TABLE
        session.add(employee)
        session.commit()

        # RETURN POST ON POSTMAN
        return jsonify(request_data)


@app.route('/recommendations', methods=['POST'])  # Registrar Indicações — OK
def register_recommendations():
    # data gotten from POST BODY Json - Postman
    request_data = request.get_json()

    if "recommendation" not in request_data:
        return {"status": 400, "recommendations": "Recommendation is a mandatory field"}
    else:
        recommendations = Recommendation(id=request_data["id"], recommendation=request_data["recommendation"])

        # INSERT DATA TO MYSQL TABLE
        session.add(recommendations)
        session.commit()

        # RETURN ON POSTMAN
        return jsonify(request_data)


@app.route('/teams', methods=['GET'])
def get_all_teams():
    team_schema = TeamSchema()
    #res = session.query(Team).join(Employee).filter(Team.id == Employee.team_id).all()
    res = session.query(Team).all()

    print(f'RES: {res}')
    res_json = team_schema.dump(res, many=True)
    print('RESJSON: ', res_json)
    return jsonify(res_json)


@app.route('/recommendations', methods=['GET'])  # Retornar uma lista de indicações — OK
def get_all_recommendations():
    reco_schema = RecoSchema()
    res = session.query(Recommendation).all()
    res_json = reco_schema.dump(res, many=True)
    return jsonify(res_json)


@app.route('/recommendations/employees', methods=['GET'])
def get_all_employees_with_recommendations():
    return_dict = {"example": "List employees!"}

    return jsonify(return_dict)


if __name__ == "__main__":
    app.run(debug=True)
