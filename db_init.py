from flask import Flask
from models import db, Product
from faker import Faker
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecom.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

fake = Faker()

def seed_products():
    with app.app_context():
        db.drop_all()
        db.create_all()

        categories = ['Smartphones', 'Laptops', 'Accessories', 'Audio', 'Wearables']
        for _ in range(100):
            product = Product(
                name=fake.word().capitalize() + " " + fake.word().capitalize(),
                category=random.choice(categories),
                price=round(random.uniform(5000, 80000), 2),
                description=fake.sentence(nb_words=10),
                image_url=fake.image_url(width=350, height=200)
            )
            db.session.add(product)

        db.session.commit()
        print("✅ Database seeded with 100+ mock products.")

if __name__ == '__main__':
    seed_products()
