import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Retrieve environment variables
PYWEBVIEW_GUI = os.getenv("PYWEBVIEW_GUI","qt")
DEFAULT_HOST = os.getenv("DEFAULT_HOST", "127.0.0.1")
TRADING_PORT = int(os.getenv("TRADING_PORT", 7497))
LIVE_TRADING_PORT = int(os.getenv("LIVE_TRADING_PORT", 7497))
DEFAULT_CLIENT_ID = int(os.getenv("DEFAULT_CLIENT_ID", 0))
INITIAL_SYMBOL = os.getenv("INITIAL_SYMBOL", "AAPL")
LIVE_TRADING = False
if LIVE_TRADING:
    TRADING_PORT = LIVE_TRADING_PORT

# Other constants
# Default timeframe for chart
DEFAULT_TIMEFRAME = "1 min" # Default timeframe for chart
DEFAULT_TIMEFRAME_OPTIONS = ('1 min', '5 mins', '15 mins', '1 hour')
# Timeout for queue operations
DATA_QUEUE_TIMEOUT = 5 
# Default duration for historical data requests
DEFAULT_HISTORICAL_DURATION = os.getenv("DEFAULT_HISTORICAL_DURATION", "30 D")
# Default currency for trading
DEFAULT_CURRENCY = os.getenv("DEFAULT_CURRENCY", "USD")


