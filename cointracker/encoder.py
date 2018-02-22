import json
import datetime

class MyEncoder(json.JSONEncoder):
    '''
        Usage, when you call a json.dumps(), call like
        json.dumps(obj, cls = MyEncoder), to convert json
        objects to str object
    '''
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime("%s")
        return json.JSONEncoder.default(self, obj)