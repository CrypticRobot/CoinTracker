# Schedule Cron Job
import atexit
from cointracker import app, okcoinSpot
from cointracker.transactions import cron_store_history_prices
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

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
]


for each in min_jobs:
    scheduler.add_job(
        func=cron_store_history_prices,
        trigger=IntervalTrigger(minutes=5),
        args=[okcoinSpot, each['target'], each['against']],
        kwargs={'since': None, 'time_elapse':each['time_elapse'], 'time_unit':each['time_unit']},
        id='_'.join([each['target'], each['against'], str(each['time_elapse']), each['time_unit']]),
        name='Periodical: {}'.format('_'.join([each['target'], each['against'], str(each['time_elapse']), each['time_unit']])),
        max_instances=10,
        replace_existing=True,
        jitter=10
    )

for each in day_jobs:
    scheduler.add_job(
        func=cron_store_history_prices,
        trigger=IntervalTrigger(minutes=11),
        args=[okcoinSpot, each['target'], each['against']],
        kwargs={'since': None, 'time_elapse':each['time_elapse'], 'time_unit':each['time_unit']},
        id='_'.join([each['target'], each['against'], str(each['time_elapse']), each['time_unit']]),
        name='Periodical: {}'.format('_'.join([each['target'], each['against'], str(each['time_elapse']), each['time_unit']])),
        max_instances=10,
        replace_existing=True,
        jitter=10
    )

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())