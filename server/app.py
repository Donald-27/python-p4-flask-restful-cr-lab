#!/usr/bin/env python3

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

# Setup app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

# Setup extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)

# Import model after db is defined
from models import Plant

# ROUTES
@app.route('/')
def index():
    return '<h1>Virtual Care Plant Store</h1>'

# GET /plants
@app.route('/plants', methods=['GET'])
def get_plants():
    plants = Plant.query.all()
    return jsonify([plant.to_dict() for plant in plants]), 200

# GET /plants/<int:id>
@app.route('/plants/<int:id>', methods=['GET'])
def get_plant_by_id(id):
    plant = Plant.query.get_or_404(id)
    return jsonify(plant.to_dict()), 200

# POST /plants
@app.route('/plants', methods=['POST'])
def create_plant():
    data = request.get_json()

    if not data or not all(key in data for key in ("name", "image", "price")):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        new_plant = Plant(name=data['name'], image=data['image'], price=data['price'])
        db.session.add(new_plant)
        db.session.commit()
        return jsonify(new_plant.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5555, debug=True)
