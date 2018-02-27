# Schedule Cron Job
import atexit
from cointracker import okcoinSpot
from cointracker.transactions import (
    cron_store_history_prices,
    calculate_all_slopes
)
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
        'time_elapse': 1,
        'time_unit': 'min',
        'jitter': 10,
    },
    {
        'target': 'eth',
        'against': 'btc',
        'time_elapse': 1,
        'time_unit': 'min',
        'jitter': 10,
    },
    {
        'target': 'bch',
        'against': 'btc',
        'time_elapse': 1,
        'time_unit': 'min',
        'jitter': 10,
    },
    {
        'target': 'etc',
        'against': 'btc',
        'time_elapse': 1,
        'time_unit': 'min',
        'jitter': 10,
    },
    {
        'target': 'btc',
        'against': 'usdt',
        'time_elapse': 1,
        'time_unit': 'min',
        'jitter': 10,
    },
    {
        'target': 'ltc',
        'against': 'usdt',
        'time_elapse': 1,
        'time_unit': 'min',
        'jitter': 10,
    },
    {
        'target': 'eth',
        'against': 'usdt',
        'time_elapse': 1,
        'time_unit': 'min',
        'jitter': 10,
    },
    {
        'target': 'bch',
        'against': 'usdt',
        'time_elapse': 1,
        'time_unit': 'min',
        'jitter': 10,
    },
    {
        'target': 'etc',
        'against': 'usdt',
        'time_elapse': 1,
        'time_unit': 'min',
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

slope_jobs = [
    {
        'target': 'btc',
        'against': 'usdt',
        'window_size': 15,
    },
    {
        'target': 'btc',
        'against': 'usdt',
        'window_size': 20,
    },
    {
        'target': 'btc',
        'against': 'usdt',
        'window_size': 30,
    },
    {
        'target': 'btc',
        'against': 'usdt',
        'window_size': 60,
    },
    {
        'target': 'ltc',
        'against': 'usdt',
        'window_size': 15,
    },
    {
        'target': 'ltc',
        'against': 'usdt',
        'window_size': 20,
    },
    {
        'target': 'ltc',
        'against': 'usdt',
        'window_size': 30,
    },
    {
        'target': 'ltc',
        'against': 'usdt',
        'window_size': 60,
    },
]

for each in slope_jobs:
    id = '_'.join([each['target'], each['against'], str(each['window_size'])])
    scheduler.add_job(
        func=calculate_all_slopes,
        trigger=CronTrigger(second=49),
        args=[each['window_size'], each['target'], each['against']],
        id=id,
        name='Slope: {}'.format(id),
        replace_existing=True,
    )

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
