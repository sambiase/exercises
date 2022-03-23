from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from projetoSim.scratches import secrets


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root:{secrets.password}@localhost/flask_sqlalchemy'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
ma = Marshmallow(app)


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(50))


class TeamSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Team

@app.route('/teams', methods=['GET'])
def get_teams():
    one_team = Team.query.first()
    team_schema= TeamSchema()
    resTeam = team_schema.dump(one_team).data
    return jsonify({"id": resTeam})


if __name__ == '__main__':
    app.run(debug=True)
