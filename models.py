from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    category = db.Column(db.String(50))
    price = db.Column(db.Float)
    description = db.Column(db.Text)
    image_url = db.Column(db.String(200))

class Conversation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_message = db.Column(db.Text)
    bot_response = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
