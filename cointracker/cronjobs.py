# Schedule Cron Job
import atexit
from cointracker import okcoinSpot
from cointracker.transactions import cron_store_history_prices
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import logging

logging.getLogger('apscheduler').setLevel(logging.DEBUG)
scheduler = BackgroundScheduler()
scheduler.start()

min_jobs = [
    {
        'target': 'ltc',
        'against': 'btc',
        'time_elapse': 5,
        'time_unit': 'min',
        'jitter': 10,
    },
    {
        'target': 'eth',
        'against': 'btc',
        'time_elapse': 5,
        'time_unit': 'min',
        'jitter': 10,
    },
    {
        'target': 'bch',
        'against': 'btc',
        'time_elapse': 5,
        'time_unit': 'min',
        'jitter': 10,
    },
    {
        'target': 'etc',
        'against': 'btc',
        'time_elapse': 5,
        'time_unit': 'min',
        'jitter': 10,
    },
    {
        'target': 'btc',
        'against': 'usdt',
        'time_elapse': 5,
        'time_unit': 'min',
        'jitter': 10,
    },
    {
        'target': 'ltc',
        'against': 'usdt',
        'time_elapse': 5,
        'time_unit': 'min',
        'jitter': 10,
    },
    {
        'target': 'eth',
        'against': 'usdt',
        'time_elapse': 5,
        'time_unit': 'min',
        'jitter': 10,
    },
    {
        'target': 'bch',
        'against': 'usdt',
        'time_elapse': 5,
        'time_unit': 'min',
        'jitter': 10,
    },
    {
        'target': 'etc',
        'against': 'usdt',
        'time_elapse': 5,
        'time_unit': 'min',
        'jitter': 10,
    },
]

hour_jobs = [
    {
        'target': 'ltc',
        'against': 'btc',
        'time_elapse': 1,
        'time_unit': 'hour',
        'jitter': 10,
    },
    {
        'target': 'eth',
        'against': 'btc',
        'time_elapse': 1,
        'time_unit': 'hour',
        'jitter': 10,
    },
    {
        'target': 'bch',
        'against': 'btc',
        'time_elapse': 1,
        'time_unit': 'hour',
        'jitter': 10,
    },
    {
        'target': 'etc',
        'against': 'btc',
        'time_elapse': 1,
        'time_unit': 'hour',
        'jitter': 10,
    },
    {
        'target': 'btc',
        'against': 'usdt',
        'time_elapse': 1,
        'time_unit': 'hour',
        'jitter': 10,
    },
    {
        'target': 'ltc',
        'against': 'usdt',
        'time_elapse': 1,
        'time_unit': 'hour',
        'jitter': 10,
    },
    {
        'target': 'eth',
        'against': 'usdt',
        'time_elapse': 1,
        'time_unit': 'hour',
        'jitter': 10,
    },
    {
        'target': 'bch',
        'against': 'usdt',
        'time_elapse': 1,
        'time_unit': 'hour',
        'jitter': 10,
    },
    {
        'target': 'etc',
        'against': 'usdt',
        'time_elapse': 1,
        'time_unit': 'hour',
        'jitter': 10,
    },
]

day_jobs = [
    {
        'target': 'ltc',
        'against': 'btc',
        'time_elapse': 1,
        'time_unit': 'day',
        'jitter': 10,
    },
    {
        'target': 'eth',
        'against': 'btc',
        'time_elapse': 1,
        'time_unit': 'day',
        'jitter': 10,
    },
    {
        'target': 'bch',
        'against': 'btc',
        'time_elapse': 1,
        'time_unit': 'day',
        'jitter': 10,
    },
    {
        'target': 'etc',
        'against': 'btc',
        'time_elapse': 1,
        'time_unit': 'day',
        'jitter': 10,
    },
    {
        'target': 'btc',
        'against': 'usdt',
        'time_elapse': 1,
        'time_unit': 'day',
        'jitter': 10,
    },
    {
        'target': 'ltc',
        'against': 'usdt',
        'time_elapse': 1,
        'time_unit': 'day',
        'jitter': 10,
    },
    {
        'target': 'eth',
        'against': 'usdt',
        'time_elapse': 1,
        'time_unit': 'day',
        'jitter': 10,
    },
    {
        'target': 'bch',
        'against': 'usdt',
        'time_elapse': 1,
        'time_unit': 'day',
        'jitter': 10,
    },
    {
        'target': 'etc',
        'against': 'usdt',
        'time_elapse': 1,
        'time_unit': 'day',
        'jitter': 10,
    },
]

for each in min_jobs:
    id = '_'.join([
        each['target'],
        each['against'],
        str(each['time_elapse']),
        each['time_unit']]
    )
    scheduler.add_job(
        func=cron_store_history_prices,
        trigger=CronTrigger(second=15),  # every minute 15 seconds point
        args=[okcoinSpot, each['target'], each['against']],
        kwargs={'since': None,
                'time_elapse': each['time_elapse'],
                'time_unit': each['time_unit']},
        id=id,
        name='Price/min: {}'.format(id),
        replace_existing=True,
    )

for each in hour_jobs:
    id = '_'.join([
        each['target'],
        each['against'],
        str(each['time_elapse']),
        each['time_unit']]
    )
    scheduler.add_job(
        func=cron_store_history_prices,
        trigger=CronTrigger(second=59),
        args=[okcoinSpot, each['target'], each['against']],
        kwargs={'since': None,
                'time_elapse': each['time_elapse'],
                'time_unit': each['time_unit']},
        id=id,
        name='Price/min: {}'.format(id),
        replace_existing=True,
    )

for each in day_jobs:
    id = '_'.join([
        each['target'],
        each['against'],
        str(each['time_elapse']),
        each['time_unit']]
    )
    scheduler.add_job(
        func=cron_store_history_prices,
        trigger=CronTrigger(second=45),  # every minute 45 seconds point
        args=[okcoinSpot, each['target'], each['against']],
        kwargs={'since': None,
                'time_elapse': each['time_elapse'],
                'time_unit': each['time_unit']},
        id=id,
        name='Price/day: {}'.format(id),
        replace_existing=True,
    )

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())
