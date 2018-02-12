from flask_sqlalchemy import SQLAlchemy
from cointracker import app
import time
time.sleep(3)  # wait for DB to start

db = SQLAlchemy(app)

class Price(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    target = db.Column(db.String(10), nullable=False)
    against = db.Column(db.String(10), nullable=False)
    price = db.Column(db.Float, nullable=False)
    

if app.config['DROP_ALL_TABLES_ON_START']:
    db.drop_all()

db.create_all()