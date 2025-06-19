from config import app, db
from models import Plant

with app.app_context():
    print("Seeding data...")

    Plant.query.delete()

    plant1 = Plant(name="Aloe", image="./images/aloe.jpg", price=11.50)
    plant2 = Plant(name="ZZ Plant", image="./images/zz-plant.jpg", price=25.98)

    db.session.add_all([plant1, plant2])
    db.session.commit()
    print("Seeded successfully!")
