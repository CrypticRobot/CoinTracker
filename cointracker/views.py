import time
import datetime
from flask import make_response, request, url_for, jsonify, redirect
from cointracker import app, okcoinSpot
from cointracker.transactions import store_history_prices, query_records
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
    
    records = query_records(
        form.target.data, 
        form.against.data, 
        time_elapse=time_elapse, 
        time_unit=time_unit, 
        before=before, 
        after=after, 
        limit=limit
    )
    prices = [x.to_dict() for x in records]
    return jsonify({
        'success': True,
        'count': len(records),
        'prices': prices,
    })