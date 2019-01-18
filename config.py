import os
''' flask debug config'''
# Flask Config
DEBUG = True

# Must override with your 'config.py' in 'instance' folder
OK_API_SITE = os.getenv('OK_API_SITE')
OK_API_PK = os.getenv('OK_API_PK')  # Public key (access key)
OK_API_SK = os.getenv('OK_API_SK')  # Secret Key (access secret)
OK_ENABLE_TRADE = False # Enable trade functions

# Database Configuration
# Set to: mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>
SQLALCHEMY_DATABASE_URI = None
SQLALCHEMY_TRACK_MODIFICATIONS = False
# Clean Start of Database
DROP_ALL_TABLES_ON_START = True
