# server/seed.py

from app import app
from models import db, Plant

with app.app_context():
    Plant.query.delete()

    p1 = Plant(name="Aloe", image="./images/aloe.jpg", price=11.50)
    p2 = Plant(name="ZZ Plant", image="./images/zz-plant.jpg", price=25.98)

    db.session.add_all([p1, p2])
    db.session.commit()
