from cointracker import app
from cointracker.okcoin import OkcoinSpotAPI


@app.route('/hello')
def hello():
    return 'Hello World'


@app.route('/test')
def test():
    ''' Test the connection to okcoin exchange '''
    site = app.config['API_SITE']
    pk = app.config['API_PK']
    sk = app.config['API_SK']

    if not pk or not sk:
        return 'error: Set public key and secret key first'

    okcoinSpot = OkcoinSpotAPI.OKCoinSpot(site, pk, sk)
    if okcoinSpot.ticker('btc_usd'):
        return 'okex success.'
    else:
        return 'okex failed.'
