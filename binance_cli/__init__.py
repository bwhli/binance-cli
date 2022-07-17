__version__ = "0.1.0"
from dotenv import dotenv_values
from rich import print

ENV = dotenv_values(".env")

if "API_KEY" not in ENV.keys() and "SECRET_KEY" not in ENV.keys():
    print(
        "Error: Please configure API_KEY and SECRET_KEY environment variables to use binance-cli."
    )
    exit()
