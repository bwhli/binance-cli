import typer

from binance_cli.binance_client import BinanceClient

app = typer.Typer()


@app.command()
def debug():
    print(__name__)


@app.command()
def buy_limit(
    market: str = typer.Argument(
        ...,
        help="The market where you want to execute the order (e.g. BTCUSDT, ETHUSDT, etc.).",
    ),
    amount: float = typer.Argument(..., help="The amount of the asset to withdraw."),
    price: str = typer.Argument(..., help="The order execution price."),
):
    binance_client = BinanceClient()
    result = binance_client.buy_limit(market.upper(), amount, price)
    print(result)


@app.command()
def buy_market(
    market: str = typer.Argument(
        ...,
        help="The market where you want to execute the order (e.g. BTCUSDT, ETHUSDT, etc.).",
    ),
    amount: float = typer.Argument(..., help="The amount of the asset to withdraw."),
):
    binance_client = BinanceClient()
    result = binance_client.buy_market(market.upper(), amount)
    print(result)


@app.command()
def sell_limit(
    market: str = typer.Argument(
        ...,
        help="The market where you want to execute the order (e.g. BTCUSDT, ETHUSDT, etc.).",
    ),
    amount: float = typer.Argument(..., help="The amount of the asset to withdraw."),
    price: str = typer.Argument(..., help="The order execution price."),
):
    binance_client = BinanceClient()
    result = binance_client.sell_limit(market.upper(), amount, price)
    print(result)


@app.command()
def sell_market(
    market: str = typer.Argument(
        ...,
        help="The market where you want to execute the order (e.g. BTCUSDT, ETHUSDT, etc.).",
    ),
    amount: float = typer.Argument(..., help="The amount of the asset to withdraw."),
):
    binance_client = BinanceClient()
    result = binance_client.sell_market(market.upper(), amount)
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
    result = binance_client.withdraw(asset.upper(), amount, address, address_tag)
    print(result)
