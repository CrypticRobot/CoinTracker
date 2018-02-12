from cointracker import app
from cointracker.okcoin import OkcoinSpotAPI

@app.route('/hello')
def hello():
    return 'Hello World'


@app.route('/test')
def test():
    ''' Test the connection to okcoin exchange '''
    site = app.config['OK_API_SITE']
    pk = app.config['OK_API_PK']
    sk = app.config['OK_API_SK']

    if not pk or not sk:
        return 'error: Set public key and secret key first'

    okcoinSpot = OkcoinSpotAPI.OKCoinSpot(site, pk, sk)
    if okcoinSpot.kline():
        return 'okex success.'
    else:
        return 'okex failed.'
