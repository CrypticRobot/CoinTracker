from flask_sqlalchemy import SQLAlchemy
from cointracker import app
import time
time.sleep(3)  # wait for DB to start

db = SQLAlchemy(app)

class Price(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # price spot date time
    date = db.Column(db.DateTime, nullable=False)
    # source currency
    target = db.Column(db.String(10), nullable=False)
    # target currency
    against = db.Column(db.String(10), nullable=False)
    # 1,2,3
    time_elapse = db.Column(db.Integer, nullable=False)
    # min, hour, week, month, year
    time_unit = db.Column(db.String(10), nullable=False)
    # price candle and volume
    start = db.Column(db.Float, nullable=False)
    high = db.Column(db.Float, nullable=False)
    low = db.Column(db.Float, nullable=False)
    end = db.Column(db.Float, nullable=False)
    volume = db.Column(db.Float, nullable=False)


if app.config['DROP_ALL_TABLES_ON_START']:
    db.drop_all()

db.create_all()