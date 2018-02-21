import time
import datetime
from cointracker import app
from cointracker.okcoin import OkcoinSpotAPI
from cointracker.transactions import store_history_prices

site = app.config['OK_API_SITE']
pk = app.config['OK_API_PK']
sk = app.config['OK_API_SK']

if app.config['OK_ENABLE_TRADE']:
    if not pk or not sk:
        raise ValueError('error: Set public key and secret key first')

okcoinSpot = OkcoinSpotAPI.OKCoinSpot(site, pk, sk)

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
