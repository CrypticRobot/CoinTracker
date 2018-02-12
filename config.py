''' flask debug config'''
# Flask Config
DEBUG = True

# These secret variables  Must be override with your 'config.py' in 'instance' folder
OK_API_SITE = None
OK_API_PK = None  # Public key (access key)
OK_API_SK = None  # Secret Key (access secret)

# Database Configuration
SQLALCHEMY_DATABASE_URI = None
# Set to: mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Clean Start of Database
DROP_ALL_TABLES_ON_START = True
