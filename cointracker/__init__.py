from flask import Flask
import os
import jinja2


# Flask
app = Flask(__name__, static_folder='static', template_folder='templates', instance_relative_config=True)
app.config.from_object('config')  # Load app config
app.config.from_pyfile('config.py')  # Load instance specifig config (secrets)

# Jinja2
TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')
JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR))

# Views of app
import cointracker.views
