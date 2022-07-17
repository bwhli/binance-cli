import typer
from binance.client import Client
from binance.enums import *
from binance.exceptions import BinanceAPIException

from binance_cli import ENV


class BinanceClient:

    BINANCE_API_KEY = ENV["API_KEY"]
    BINANCE_SECRET_KEY = ENV["SECRET_KEY"]

    def __init__(self) -> None:
        self.client = Client(self.BINANCE_API_KEY, self.BINANCE_SECRET_KEY)

    def buy_limit(self, market: str, amount: float, price: str):
        try:
            result = self.client.order_limit_buy(
                symbol=market.upper(), quantity=amount, price=str(price)
            )
            return result
        except BinanceAPIException as e:
            print(e)
            raise typer.Exit()

    def buy_market(self, market: str, amount: float):
        try:
            result = self.client.create_order(
                symbol=market.upper(),
                side=SIDE_BUY,
                type=ORDER_TYPE_MARKET,
                quantity=amount,
            )
            return result
        except BinanceAPIException as e:
            print(e)
            raise typer.Exit()

    def sell_limit(self, market: str, amount: float, price: str):
        try:
            result = self.client.order_limit_sell(
                symbol=market.upper(), quantity=amount, price=str(price)
            )
            return result
        except BinanceAPIException as e:
            print(e)
            raise typer.Exit()

    def sell_market(self, market: str, amount: float):
        try:
            result = self.client.create_order(
                symbol=market.upper(),
                side=SIDE_SELL,
                type=ORDER_TYPE_MARKET,
                quantity=amount,
            )
            return result
        except BinanceAPIException as e:
            print(e)
            raise typer.Exit()

    def withdraw(
        self,
        asset: str,
        amount: float,
        address: str,
        address_tag: str = None,
        network=None,
    ):
        try:
            result = self.client.withdraw(
                coin=asset.upper(),
                address=address,
                amount=amount,
                addressTag=address_tag,
                network=network,
            )
            return result
        except BinanceAPIException as e:
            print(e)
            raise typer.Exit()
