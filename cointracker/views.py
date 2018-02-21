import time
import datetime
from cointracker import app, okcoinSpot
from cointracker.transactions import store_history_prices


@app.route('/hello')
def hello():
    return 'Hello World'


@app.route('/test/<string:target>/<string:against>')
def test(target, against):
    ''' Test the connection to okcoin exchange '''
    since = datetime.datetime(2017, 12, 1, hour=0, minute=0)
    try:
        fetched, stored = store_history_prices(okcoinSpot, target, against, since)
        return 'fetched {}, stored {}'.format(fetched, stored)
    except ValueError as e:
        return 'Test failed, {}'.format(e)
