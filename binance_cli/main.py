import typer

from binance_cli.binance_client import BinanceClient

app = typer.Typer()


@app.command()
def debug():
    print(__name__)


@app.command()
def buy_market(
    market: str = typer.Argument(
        ...,
        help="The market where you want to execute the order (e.g. BTCUSDT, ETHUSDT, etc.).",
    ),
    amount: float = typer.Argument(..., help="The amount of the asset to withdraw."),
):
    binance_client = BinanceClient()
    result = binance_client.buy_market(market, amount)
    print(result)


@app.command()
def withdraw(
    asset: str = typer.Argument(
        ..., help="The symbol of the asset to withdraw (e.g. BTC, ETH, USDC)."
    ),
    amount: float = typer.Argument(..., help="The amount of the asset to withdraw."),
    address: str = typer.Argument(..., help="The wallet address to withdraw to."),
    address_tag: str = typer.Argument(None, help="The tag or memo if required."),
):
    binance_client = BinanceClient()
    result = binance_client.withdraw(asset, amount, address, address_tag)
    print(result)
