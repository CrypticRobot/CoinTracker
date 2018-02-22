import time
import datetime
from flask import make_response, request, url_for, jsonify, redirect
from cointracker import app, okcoinSpot, JINJA_ENVIRONMENT
from cointracker.transactions import store_history_prices, query_records, query_a_record
import cointracker.forms as forms
import logging

@app.route('/hello')
def hello():
    return 'Hello World'


@app.route('/test')
def test():
    try:
        result = okcoinSpot.ticker(symbol='ltc_btc')
        if result:
            return 'test ok' + str(result)
    except:
        return 'test failed'


@app.route('/api/price')
def api_price():
    form = forms.APIPrice(request.args)
    if not form.validate():
        return jsonify({'success': False, 'error': 'parameter error'})
    
    before = datetime.datetime.fromtimestamp(form.before.data) if form.before.data else None
    after = datetime.datetime.fromtimestamp(form.after.data) if form.after.data else None
    time_elapse = form.time_elapse.data if form.time_elapse.data else 1
    time_unit = form.time_unit.data if form.time_unit.data else 'min'
    limit = form.limit.data if form.limit.data else 100
    newest = form.newest.data if form.newest.data else True
    
    records = query_records(
        form.target.data, 
        form.against.data, 
        time_elapse=time_elapse, 
        time_unit=time_unit, 
        before=before, 
        after=after, 
        limit=limit,
        newest=newest
    )
    prices = [x.to_dict() for x in records]
    if newest:
        prices = prices[::-1]
    
    return jsonify({
        'success': True,
        'count': len(records),
        'result': prices,
    })

@app.route('/api/price/first')
def api_first():
    form = forms.APISingle(request.args)
    if not form.validate():
        return jsonify({'success': False, 'error': 'parameter error'})
    
    time_elapse = form.time_elapse.data if form.time_elapse.data else 1
    time_unit = form.time_unit.data if form.time_unit.data else 'min'

    record = query_a_record(form.target.data, form.against.data, time_elapse=time_elapse, time_unit=time_unit, order='ASC')
    return jsonify({
        'success': True,
        'result': record.to_dict() if record else None,
    })

@app.route('/api/price/last')
def api_last():
    form = forms.APISingle(request.args)
    if not form.validate():
        return jsonify({'success': False, 'error': 'parameter error'})
    
    time_elapse = form.time_elapse.data if form.time_elapse.data else 1
    time_unit = form.time_unit.data if form.time_unit.data else 'min'

    record = query_a_record(form.target.data, form.against.data, time_elapse=time_elapse, time_unit=time_unit, order='DESC')
    return jsonify({
        'success': True,
        'result': record.to_dict() if record else None,
    })

@app.route('/web/demo')
def web_demo():
    ''' Demo of a series of line dotted charts '''
    template = JINJA_ENVIRONMENT.get_template('demo.html')
    return template.render({
        'get_price_url': url_for('api_price'),
        'charts':[
            {
                'target': 'btc',
                'against': 'usdt',
                'time_unit': 'min',
                'limit': 120,
                'chartid': 'btc_usdt_min',
                'showDate': False,
                'showTime': True,
            },
            {
                'target': 'btc',
                'against': 'usdt',
                'time_unit': 'day',
                'limit': 90,
                'chartid': 'btc_usdt_day',
                'showDate': True,
                'showTime': False,
            },
            {
                'target': 'ltc',
                'against': 'usdt',
                'time_unit': 'min',
                'limit': 120,
                'chartid': 'ltc_usdt_min',
                'showDate': False,
                'showTime': True,
            },
            {
                'target': 'ltc',
                'against': 'usdt',
                'time_unit': 'day',
                'limit': 90,
                'chartid': 'ltc_usdt_day',
                'showDate': True,
                'showTime': False,
            },
            {
                'target': 'eth',
                'against': 'usdt',
                'time_unit': 'min',
                'limit': 120,
                'chartid': 'eth_usdt_min',
                'showDate': False,
                'showTime': True,
            },
            {
                'target': 'eth',
                'against': 'usdt',
                'time_unit': 'day',
                'limit': 90,
                'chartid': 'eth_usdt_day',
                'showDate': True,
                'showTime': False,
            },
            {
                'target': 'bch',
                'against': 'usdt',
                'time_unit': 'min',
                'limit': 120,
                'chartid': 'bch_usdt_min',
                'showDate': False,
                'showTime': True,
            },
            {
                'target': 'bch',
                'against': 'usdt',
                'time_unit': 'day',
                'limit': 90,
                'chartid': 'bch_usdt_day',
                'showDate': True,
                'showTime': False,
            },
            {
                'target': 'ltc',
                'against': 'btc',
                'time_unit': 'min',
                'limit': 120,
                'chartid': 'ltc_btc_min',
                'showDate': False,
                'showTime': True,
            },
            {
                'target': 'ltc',
                'against': 'btc',
                'time_unit': 'day',
                'limit': 90,
                'chartid': 'ltc_btc_day',
                'showDate': True,
                'showTime': False,
            },
            {
                'target': 'eth',
                'against': 'btc',
                'time_unit': 'min',
                'limit': 120,
                'chartid': 'eth_btc_min',
                'showDate': False,
                'showTime': True,
            },
            {
                'target': 'eth',
                'against': 'btc',
                'time_unit': 'day',
                'limit': 90,
                'chartid': 'eth_btc_day',
                'showDate': True,
                'showTime': False,
            },
            {
                'target': 'bch',
                'against': 'btc',
                'time_unit': 'min',
                'limit': 120,
                'chartid': 'bch_btc_min',
                'showDate': False,
                'showTime': True,
            },
            {
                'target': 'bch',
                'against': 'btc',
                'time_unit': 'day',
                'limit': 90,
                'chartid': 'bch_btc_day',
                'showDate': True,
                'showTime': False,
            },
        ]
    })