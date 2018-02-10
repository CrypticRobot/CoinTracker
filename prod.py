''' Production App '''
import cointracker
my_app = cointracker.app

# Fix the proxy headers issue
from werkzeug.contrib.fixers import ProxyFix
my_app.wsgi_app = ProxyFix(my_app.wsgi_app)
