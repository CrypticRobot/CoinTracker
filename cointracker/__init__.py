import os
import jinja2
from flask import Flask


# Flask Config
app = Flask(__name__, static_folder='static', template_folder='templates', instance_relative_config=True)
app.config.from_object('config')  # Load app config
app.config.from_pyfile('config.py')  # Load instance specifig config (secrets)

# Database Config
db_configs = {
    'user': os.environ['MYSQL_USER'],
    'password': os.environ['MYSQL_PASSWORD'],
    'host': os.environ['MYSQL_HOST'],
    'port': os.environ['MYSQL_PORT'],
    'dbname': os.environ['MYSQL_DB_NAME'],
}
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{dbname}'.format(**db_configs)

# Jinja2
TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')
JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR))

# OKEX Client
from cointracker.okcoin import OkcoinSpotAPI
site = app.config['OK_API_SITE']
pk = app.config['OK_API_PK']
sk = app.config['OK_API_SK']

if app.config['OK_ENABLE_TRADE']:
    if not pk or not sk:
        raise ValueError('error: Set public key and secret key first')

okcoinSpot = OkcoinSpotAPI.OKCoinSpot(site, pk, sk)

# Views of app
import cointracker.views

# Database of app
import cointracker.database

# Cron jobs
import cointracker.cronjobs

# JSON Encoder
# Flask Json Config
import cointracker.encoder
app.json_encoder = cointracker.encoder.MyEncoder