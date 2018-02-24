''' Database Transactions '''
import datetime
from cointracker.database import db, Price, CronJob

supported_symbols = [
    "ltc_btc",
    "eth_btc",
    "etc_btc",
    "bch_btc",
    "btc_usdt",
    "eth_usdt",
    "ltc_usdt",
    "etc_usdt",
    "bch_usdt",
    "etc_eth",
    "bt1_btc",
    "bt2_btc",
    "btg_btc",
    "qtum_btc",
    "hsr_btc",
    "neo_btc",
    "gas_btc",
    "qtum_usdt",
    "hsr_usdt",
    "neo_usdt",
    "gas_usd",
]

supported_types = [
    '1min',
    '3min',
    '5min',
    '15min',
    '30min',
    '1day',
    '3day',
    '1week',
    '1hour',
    '2hour',
    '4hour',
    '6hour',
    '12hour',
]


def store_history_prices(okcoinSpot, target, against, since=None, time_elapse=1, time_unit='min'):
    ''' fetch around 2000 spot prices each time
    raise ValueError if target and against is not supported
    raise ValueError if time_elapse and time_unit is not supported
    Parameters
    ----------
    okcoinSpot: OKCoinSpot
        a client for okcoin spot price calling
    target: string 
        ltc, btc ...
    against: string
        usdt, btc ...
    since: datetime object (accurate to minute)

    Returns
    -------
    int, int: (actual lines fetched, actual lines stored)
    '''
    symbol = '_'.join([target, against])
    if symbol not in supported_symbols:
        raise ValueError("{}_{} pair not in support list".format(target, against))
    
    time_type = ''.join([str(time_elapse), time_unit])
    if time_type not in supported_types:
        raise ValueError("{}_{} pair not in support list".format(time_elapse, time_unit))
    
    if since:
        since = int(since.strftime("%s")) * 1000
        lines = okcoinSpot.kline(symbol=symbol, time_type=time_type, since=since)
    else:
        lines = okcoinSpot.kline(symbol=symbol, time_type=time_type)
    inserted = 0
    for line in lines:
        already = Price.query.filter_by(date=datetime.datetime.fromtimestamp(line[0]/1000), target=target, against=against, time_elapse=time_elapse, time_unit=time_unit).first()
        if not already:
            price = Price(
                date=datetime.datetime.fromtimestamp(line[0]/1000),
                target=target,
                against=against,
                time_elapse=time_elapse,
                time_unit=time_unit,
                start=float(line[1]),
                high=float(line[2]),
                low=float(line[3]),
                end=float(line[4]),
                volume=float(line[5]),
            )
            db.session.add(price)
            inserted += 1
        
        db.session.commit()
    return len(lines), inserted


def cron_store_history_prices(okcoinSpot, target, against, since=None, time_elapse=1, time_unit='min'):
    ''' A cron job to fetch historical price data '''
    try:
        # Detect last old prices
        already = Price.query.filter_by(target=target, against=against, time_elapse=time_elapse, time_unit=time_unit).order_by(Price.date.desc()).first()
        if already:
            since = already.date if not since else since
        fetched, stored = store_history_prices(okcoinSpot, target, against, since, time_elapse, time_unit)
        cron_job = CronJob(
            date=datetime.datetime.utcnow(),
            fetched=fetched,
            stored=stored,
            target=target,
            against=against,
        )
        db.session.add(cron_job)
        db.session.commit()
        return fetched, stored
    except ValueError:
        return None, None


def query_records(target, against, time_elapse=1, time_unit='min', before=None, after=None, limit=100, newest=True):
    ''' Before and After shall be datetime.datetime obj
    Returns
    -------
    list: of query results
    '''
    q = Price.query.filter_by(target=target, against=against, time_elapse=time_elapse, time_unit=time_unit)
    if before:
        q = q.filter(Price.date < before)
    if after:
        q = q.filter(Price.date > after)
    if newest:
        q = q.order_by(Price.date.desc())
    else:
        q = q.order_by(Price.date)
    if limit:
        q = q.limit(limit)
    
    return q.all()

def query_a_record(target, against, time_elapse=1, time_unit='min', order='ASC'):
    ''' Before and After shall be datetime.datetime obj
    Returns
    -------
    a result, in the form of python object
    '''
    q = Price.query.filter_by(target=target, against=against, time_elapse=time_elapse, time_unit=time_unit)
    if order == 'ASC':
        q = q.order_by(Price.date)
    else:
        q = q.order_by(Price.date.desc())
    return q.first()