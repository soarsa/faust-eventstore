from decimal import Decimal
from datetime import datetime
import random
from examples.tradeexecution.commands import ExecuteTradeRequest

dummy_traders = {
    "ssmith": "Sid Smith",
    "jjones": "Jimmy Jones",
    "asmythe": "Andy Smythe",
    "vpopolus": "Vasilis Popolopodus",
    "jjones": "Jen Jones"
}

dummy_currency_pairs = [
    "EUR/USD",
    "USD/JPY",
    "GBP/USD",
    "USD/CHF",
    "USD/CAD",
    "AUD/USD",
    "NZD/USD",
]

dummy_direction = [
    "BUY",
    "SELL"
]


def create_dummy_trade_request() -> ExecuteTradeRequest:

    currency_pair: str = random.choice(dummy_currency_pairs)
    trader: str = random.choice(list(dummy_traders.keys()))
    spot_rate = Decimal(random.uniform(1.0, 2.0))
    value_date = datetime.now()
    direction: str = random.choice(dummy_direction)
    notional = Decimal(random.randint(1, 9) * 1000000)
    dealt_currency: str = currency_pair.split("/")[random.randint(0, 1)]

    return ExecuteTradeRequest(trader_name=trader,
                               currency_pair=currency_pair,
                               spot_rate=spot_rate,
                               value_date=value_date,
                               direction=direction,
                               notional= notional,
                               dealt_currency=dealt_currency)
