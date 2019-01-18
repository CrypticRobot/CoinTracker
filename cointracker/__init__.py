import os
from dotenv import load_dotenv
import jinja2
from flask import Flask
import logging
from pathlib import Path
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

logging.basicConfig(
    filename='cointracker_everything.log',
    filemode='a',
    format='[%(levelname)s][%(asctime)s][%(filename)s:%(funcName)s:%(lineno)d][%(message)s]',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO)


# Flask Config
app = Flask(__name__, static_folder='static', template_folder='templates', instance_relative_config=True)
app.config.from_object('config')  # Load app config
app.config.from_pyfile('config.py')  # Load instance specifig config (secrets)

# Database Config
db_configs = {
    'user': os.getenv( "MYSQL_USER" ),
    'password': os.getenv("MYSQL_PASSWORD"),
    'host': os.getenv("MYSQL_HOST"),
    'port': os.getenv("MYSQL_PORT"),
    'dbname': os.getenv("MYSQL_DB_NAME"),
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
