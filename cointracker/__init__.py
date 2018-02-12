import os
import jinja2
from flask import Flask


# Flask
app = Flask(__name__, static_folder='static', template_folder='templates', instance_relative_config=True)
app.config.from_object('config')  # Load app config
app.config.from_pyfile('config.py')  # Load instance specifig config (secrets)

# Database
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

# Views of app
import cointracker.views

# Database of app
import cointracker.database