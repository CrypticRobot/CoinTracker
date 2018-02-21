# CoinTracker
Flask Application Mostly For Cryptocurrency (Bitcoin) Tracking.
Language Python > 3.4

# Keys
1. OKEX `price` API ***doesn't*** need an accessKey/accessSecret.
2. OKEX `trade` API ***need*** an accessKey/accessSecret pair.

# Before You Run
1. `mkdir instance` to create a folder for your local configuration.
2. `touch instance/config.py` to create your local configurations.
3. Configurations in `instance/config.py` will override those in `config.py`

# Test/Development/Production Environement
See `/docker` folder