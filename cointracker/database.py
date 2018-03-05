from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect
from cointracker import app
import datetime
import time
time.sleep(3)  # wait for DB to start

db = SQLAlchemy(app)


class Printable():
    ''' Make SQLalchemy objects convert to python dict '''

    def to_dict(self, exclude=[]):
        insp = inspect(self.__class__)
        columns = insp.all_orm_descriptors.keys()

        columns = [x for x in columns if not x.startswith('__')]
        for x in exclude:
            columns.remove(x)

        return_dict = {}
        for y in columns:
            return_dict[y] = getattr(self, y)

        return return_dict


class Price(db.Model, Printable):
    ''' Spot price and its date'''
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)  # price spot date time
    target = db.Column(db.String(10), nullable=False)  # source currency
    against = db.Column(db.String(10), nullable=False)  # target currency
    time_elapse = db.Column(db.Integer, nullable=False)  # 1,2,3
    # min, hour, week, month, year
    time_unit = db.Column(db.String(10), nullable=False)
    # price candle and volume
    start = db.Column(db.Float, nullable=False)
    high = db.Column(db.Float, nullable=False)
    low = db.Column(db.Float, nullable=False)
    end = db.Column(db.Float, nullable=False)
    volume = db.Column(db.Float, nullable=False)
    # calculated price related field
    amplitude = db.Column(db.Float, nullable=False)  # high - low
    amp_percent = db.Column(db.Float, nullable=False)  # amplitude / start
    diff = db.Column(db.Float, nullable=False)  # end - start
    diff_percent = db.Column(db.Float, nullable=False)  # diff / start


class CronJob(db.Model, Printable):
    ''' Cron jobs results '''
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    fetched = db.Column(db.Integer, nullable=False)
    stored = db.Column(db.Integer, nullable=False)
    target = db.Column(db.String(10), nullable=False)
    against = db.Column(db.String(10), nullable=False)


if app.config['DROP_ALL_TABLES_ON_START']:
    db.drop_all()

db.create_all()
