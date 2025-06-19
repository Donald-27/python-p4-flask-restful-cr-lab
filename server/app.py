from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)

from models import Plant  # must be below db init


@app.route('/plants', methods=['GET'])
def get_plants():
    plants = Plant.query.all()
    return jsonify([plant.to_dict() for plant in plants])


@app.route('/plants', methods=['POST'])
def create_plant():
    data = request.get_json()
    plant = Plant(
        name=data.get('name'),
        image=data.get('image'),
        price=data.get('price')
    )
    db.session.add(plant)
    db.session.commit()
    return jsonify(plant.to_dict()), 201


@app.route('/plants/<int:id>', methods=['GET'])
def get_plant_by_id(id):
    plant = Plant.query.get_or_404(id)
    return jsonify(plant.to_dict())
