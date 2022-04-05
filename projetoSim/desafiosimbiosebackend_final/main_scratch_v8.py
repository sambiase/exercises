import pymysql.err
import sqlalchemy
from flask import Flask, jsonify, request, make_response
from flask_marshmallow import Marshmallow
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


# TABLE CREATION ON MYSQL - FUNCIONÁRIOS (EMPLOYEES)
class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True, nullable=False)
    employee_name = Column(String(50), nullable=False)

    team_id = Column(Integer, ForeignKey('teams.id'))
    teams = relationship('Team', back_populates='employees')

    recommendation_id = Column(Integer, ForeignKey('recommendations.id'))
    recommendations = relationship('Recommendation', back_populates='employees')

    def __repr__(self) -> str:
        return f'ID: {self.id} , Employee Name: {self.employee_name}'


# TABLE CREATION ON MYSQL - EQUIPES  (TEAMS)
class Team(Base):
    __tablename__ = 'teams'

    id = Column(Integer, primary_key=True, nullable=False)
    team_name = Column(String(50), nullable=False)

    employees = relationship('Employee', back_populates='teams')  # Employee --> references Class Employee

    def __repr__(self) -> str:
        return f'ID: {self.id}, Team Name: {self.team_name}, Employees: {self.employees}'


# TABLE CREATION ON MYSQL - INDICACOES (RECOMMENDATIONS)
class Recommendation(Base):
    __tablename__ = 'recommendations'

    id = Column(Integer, primary_key=True, nullable=False)
    recommendation = Column(String(50), nullable=False)

    employees = relationship('Employee', back_populates='recommendations')  # Employee --> references Class Employee


Base.metadata.create_all(engine)


# SERIALIZED TABLE "TEAM" SCHEMA
class TeamSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Team


# SERIALIZED TABLE "RECOMMENDATION" SCHEMA
class RecoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Recommendation


# NESTED SCHEMAS
class EmployeeTeamSchemaNested(SQLAlchemyAutoSchema):
    class Meta:
        model = Team
        include_relationships = True


# NESTED SCHEMAS
class EmployeesRecoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Recommendation
        include_relationships = True


# Registrar Equipes(times) - OK
@app.route('/teams', methods=['POST'])
def register_teams():
    # DATA GOTTEN FROM POST BODY JSON - POSTMAN
    request_data = request.get_json()

    try:
        # CHECK IF TEAM NAME WAS GIVEN
        if "team_name" not in request_data:
            session.close()
            return make_response({"status": 400, "message": "Team Name is a mandatory field"}, 400)

        else:
            teams = Team(id=request_data["id"], team_name=request_data["team_name"])

            # INSERT DATA INTO MYSQL TABLE
            session.add(teams)
            session.commit()
            session.close()

            # RETURN POST ON POSTMAN
            return make_response(jsonify({"status": 200, "message": "Team added successfully :)"}, request_data), 200)
    except:
        session.rollback()
        return make_response(jsonify({"status": 200, "message": "Column 'TEAM_NAME' cannot be null"}), 200)


# Registrar Funcionarios - OK
@app.route('/employees', methods=['POST'])
def register_employees():
    # DATA GOTTEN FROM POST BODY JSON - POSTMAN
    request_data = request.get_json()

    try:
        # CHECK IF EMPLOYEE NAME EXISTS
        if "employee_name" not in request_data:
            session.close()
            return make_response({"status": 400, "message": "Employee Name is a mandatory field"}, 400)

        else:
            employee = Employee(id=request_data["id"], employee_name=request_data["employee_name"],
                                team_id=request_data["team_id"], recommendation_id=request_data["recommendation_id"])

            # INSERT DATA TO MYSQL TABLE
            session.add(employee)
            session.commit()
            session.close()

            # RETURN POST ON POSTMAN
            return jsonify(request_data)
    except:
        session.rollback()
        return make_response(jsonify({"status": 200, "message": "Column 'EMPLOYEE NAME' cannot be null"}), 200)

# Registrar Indicações — OK
@app.route('/recommendations', methods=['POST'])
def register_recommendations():
    # data gotten from POST BODY Json - Postman
    request_data = request.get_json()

    try:
        if "recommendation" not in request_data:
            session.close()
            return make_response({"status": 400, "message": "Recommendation is a mandatory field"}, 400)

        else:
            recommendations = Recommendation(id=request_data["id"], recommendation=request_data["recommendation"])

            # INSERT DATA TO MYSQL TABLE
            session.add(recommendations)
            session.commit()
            session.close()

            # RETURN ON POSTMAN
            return make_response(
                jsonify({"status": 200, "message": "Recommendation added successfully :)"}, request_data), 200)
    except:
        session.rollback()
        return make_response(jsonify({"status": 200, "message": "Column 'RECOMMENDATION' cannot be null"}), 200)


# Retornar uma lista de equipes e respectivos funcionários — OK
@app.route('/teams', methods=['GET'])
def get_all_teams():
    team_employees = EmployeeTeamSchemaNested()
    res = session.query(Team).join(Employee).filter(Team.id == Employee.team_id).order_by(Team.id).all()
    res_json = team_employees.dump(res, many=True)
    return make_response(jsonify(res_json), 200)


# Retornar uma lista de indicações — OK
@app.route('/recommendations', methods=['GET'])
def get_all_recommendations():
    reco_schema = RecoSchema()
    res = session.query(Recommendation).all()
    res_json = reco_schema.dump(res, many=True)
    return make_response(jsonify(res_json), 200)


# Retornar quais funcionários realizaram indicações — OK
@app.route('/recommendations/employees', methods=['GET'])
def get_all_employees_with_recommendations():
    employees_reco = EmployeesRecoSchema()
    res = session.query(Recommendation).join(Employee).filter(Recommendation.id == Employee.team_id).all()
    res_json = employees_reco.dump(res, many=True)
    return make_response(jsonify(res_json), 200)


if __name__ == "__main__":
    app.run(debug=True)
