from decimal import Decimal
import uuid
from datetime import datetime, timedelta
from .aggregates import Trade


class ExecuteTradeResponse:
    def __init__(self, trade):
        self.trade = trade

    trade: Trade


class ExecuteTradeRequest:

    def __init__(self, trader_name: str, currency_pair: str, spot_rate: Decimal, value_date: datetime, direction: str,
                 notional: Decimal, dealt_currency: str):
        self.trader_name = trader_name
        self.currency_pair = currency_pair
        self.spot_rate = spot_rate
        self.value_date = value_date
        self.direction = direction
        self.notional = notional
        self.dealt_currency = dealt_currency

    trader_name: str
    currency_pair: str
    spot_rate: Decimal
    value_date: datetime
    direction: str
    notional: Decimal
    dealt_currency: str

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)


class TradeCommands:

    async def create_trade(self, request: ExecuteTradeRequest) -> ExecuteTradeResponse:

        trade_id = str(uuid.uuid4())
        trade_date = datetime.now() + timedelta(days=2)
        trade = Trade(trade_id, request.trader_name, request.currency_pair, request.spot_rate, trade_date,
                      request.value_date, request.direction, request.notional, request.dealt_currency)

        # write to repository

        # return trade from repository
        return ExecuteTradeResponse(trade)

    async def reject_trade(self, trade_id: str):
        # get from repository, invoke event
        pass

    async def trade_done(self, trade_id: int, reason: str):
        # get from repository, invoke event
        pass

