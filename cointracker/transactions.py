''' Database Transactions '''
import datetime
import logging
from cointracker.database import db, Price, CronJob, Slope

logger = logging.getLogger('transactions')
logger.setLevel(logging.DEBUG)

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
        raise ValueError(
            "{}_{} pair not in support list".format(target, against))

    time_type = ''.join([str(time_elapse), time_unit])
    if time_type not in supported_types:
        raise ValueError("{}_{} pair not in support list".format(
            time_elapse, time_unit))

    if since:
        since = int(since.strftime("%s")) * 1000
        lines = okcoinSpot.kline(
            symbol=symbol, time_type=time_type, since=since)
    else:
        lines = okcoinSpot.kline(symbol=symbol, time_type=time_type)
    inserted = 0
    for line in lines:
        already = Price.query.filter_by(
            date=datetime.datetime.fromtimestamp(line[0]/1000),
            target=target,
            against=against,
            time_elapse=time_elapse,
            time_unit=time_unit
        ).first()

        if not already:  # new data point
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
        else:  # old data point, maybe new data values?
            already.start = float(line[1])
            already.high = float(line[2])
            already.low = float(line[3])
            already.end = float(line[4])
            already.volume = float(line[5])

        db.session.commit()
    return len(lines), inserted


def cron_store_history_prices(okcoinSpot, target, against, since=None, time_elapse=1, time_unit='min'):
    ''' A cron job to fetch historical price data '''
    try:
        # Detect last old prices
        # already = Price.query.filter_by(
        #     target=target,
        #     against=against,
        #     time_elapse=time_elapse,
        #     time_unit=time_unit
        # ).order_by(Price.date.desc()).first()

        # if already:
        #     since = already.date if not since else since
        fetched, stored = store_history_prices(
            okcoinSpot, target, against, since, time_elapse, time_unit)
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
    ''' Before and After shall be datetime.datetime obj, max length of limit is 300
    Returns
    -------
    list: of query results
    '''
    q = Price.query.filter_by(
        target=target,
        against=against,
        time_elapse=time_elapse,
        time_unit=time_unit
    )

    if before:
        q = q.filter(Price.date < before)
    if after:
        q = q.filter(Price.date > after)
    if newest:
        q = q.order_by(Price.date.desc())
    else:
        q = q.order_by(Price.date)
    if limit:
        if limit > 300:
            limit = 300
        q = q.limit(limit*3)

    # deduplicate of results
    results = q.all()
    distinct_dates = []
    return_results = []
    for each in results:
        if each.date in distinct_dates:
            pass
        else:
            distinct_dates.append(each.date)
            return_results.append(each)

    if limit and len(return_results) > limit:
        return return_results[0:limit]
    else:
        return return_results


def query_a_record(target, against, time_elapse=1, time_unit='min', order='ASC'):
    ''' Before and After shall be datetime.datetime obj
    Returns
    -------
    a result, in the form of python object
    '''
    q = Price.query.filter_by(
        target=target,
        against=against,
        time_elapse=time_elapse,
        time_unit=time_unit
    )

    if order == 'ASC':
        q = q.order_by(Price.date)
    else:
        q = q.order_by(Price.date.desc())
    return q.first()


def calculate_all_slopes(window_size, target='btc', against='usdt'):
    ''' calculate the slopes of datas in database
    Parameters
    ----------
    window_size: int
        Minutes
    '''
    oldest_price = query_a_record(target, against)
    newest_price = query_a_record(target, against, order='DESC')

    last_slope_record = Slope.query.filter_by(
        target=target,
        against=against,
        duration=window_size
    ).order_by(Slope.end_date.desc()).first()

    if last_slope_record:
        window_start = last_slope_record.start_date - \
            datetime.timedelta(minutes=window_size) - \
            datetime.timedelta(minutes=100)
    else:
        window_start = oldest_price.date

    window_end = window_start + datetime.timedelta(minutes=window_size)

    if newest_price:
        logger.log(logging.DEBUG, 'newest price date: {}'.format(
            newest_price.date))
    if last_slope_record:
        logger.log(logging.DEBUG, 'last slope record end_date: {}'.format(
            last_slope_record.end_date))
    logger.log(logging.DEBUG, 'window_start {}, window_end {}'.format(
        window_start, window_end))

    total_calculate = 0
    total_skip = 0
    while(window_end <= newest_price.date):
        already = Slope.query.filter_by(
            target=target,
            against=against,
            start_date=window_start,
            end_date=window_end
        ).first()
        if not already:
            # calculate the slope, store in database
            all_prices = query_records(
                target,
                against,
                time_elapse=1,
                time_unit='min',
                before=window_end+datetime.timedelta(minutes=1),
                after=window_start+datetime.timedelta(minutes=-1),
                limit=None,
                newest=False
            )
            if all_prices:
                change = all_prices[-1].high - all_prices[0].low
                minutes_span = window_size
                slope = change / (minutes_span)
                volumes = sum([x.volume for x in all_prices])
                volumed_slope = slope * volumes

                slope_record = Slope(
                    target=target,
                    against=against,
                    change=change,
                    start_date=window_start,
                    end_date=window_end,
                    duration=minutes_span,
                    slope=slope,
                    volumed_slope=volumed_slope,
                )
                db.session.add(slope_record)
                db.session.commit()
                total_calculate += 1
            else:
                total_skip += 1
        window_start += datetime.timedelta(minutes=1)
        window_end += datetime.timedelta(minutes=1)

    logger.log(logging.DEBUG, 'total skipped: {}, total calculated: {}'.format(
        total_skip, total_calculate))


def query_last_cron_job():
    return CronJob.query.order_by(CronJob.date.desc()).first()


def query_last_slope():
    return Slope.query.order_by(Slope.end_date.desc()).first()


def count_records(target, against, time_elapse=1, time_unit='min'):
    return Price.query.filter_by(
        target=target,
        against=against,
        time_elapse=time_elapse, time_unit=time_unit).count()


def count_cron_job():
    return CronJob.query.count()


def count_slope():
    return Slope.query.count()
