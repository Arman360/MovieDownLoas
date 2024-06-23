from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app import app

db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), index=True, unique=True)
    description = db.Column(db.Text)
    release_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    rank = db.Column(db.Integer)

class TVShow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), index=True, unique=True)
    description = db.Column(db.Text)
    seasons = db.Column(db.Integer)
    episodes = db.Column(db.Integer)
    rank = db.Column(db.Integer)
