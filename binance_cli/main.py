import typer

from binance_cli.binance_client import BinanceClient

app = typer.Typer()


@app.command()
def debug():
    print(__name__)


@app.command()
def withdraw(asset: str, amount: float, address: str, address_tag: str = None):
    binance_client = BinanceClient()
    result = binance_client.withdraw(asset, amount, address, address_tag)
    print(result)
