from datetime import datetime
from decimal import Decimal
from methoddispatch import singledispatch
from eventstore.aggregatebase import AggregateBase
from .events import TradeCreatedEvent, TradeRejectedEvent, TradeCompletedEvent, TradeEventFactory
from .aggregatesmeta import TradeStatus


class Trade(AggregateBase):

    def __init__(self, trade_id: str, trader_name: str, currency_pair: str, spot_rate: Decimal, trade_date: datetime,
                 value_date: datetime, direction: str, notional: Decimal, dealt_currency: str):
        self._trade_id = trade_id
        self._trader_name = trader_name
        self._currency_pair = currency_pair
        self._spot_rate = spot_rate
        self._trade_date = trade_date
        self._value_date = value_date
        self._direction = direction
        self._notional = notional
        self._dealt_currency = dealt_currency
        self._reason = None
        self._status = TradeStatus.PENDING

        self.raise_event(TradeEventFactory.create_trade_created_event(trade_id=trade_id, trader_name=trader_name,
                                                                      currency_pair=currency_pair, spot_rate=spot_rate,
                                                                      trade_date=trade_date, value_date=value_date,
                                                                      direction=direction, notional=notional,
                                                                      dealt_currency=dealt_currency,
                                                                      status=TradeStatus.PENDING))

    @property
    def trade_id(self) -> str:
        return self._trade_id

    @property
    def trader_name(self) -> str:
        return self._trader_name

    @property
    def currency_pair(self) -> str:
        return self._currency_pair

    @property
    def spot_rate(self) -> Decimal:
        return self._spot_rate

    @property
    def trade_date(self) -> datetime:
        return self._trade_date

    @property
    def value_date(self) -> datetime:
        return self._value_date

    @property
    def direction(self) -> str:
        return self._direction

    @property
    def notional(self) -> Decimal:
        return self._notional

    @property
    def dealt_currency(self) -> str:
        return self._dealt_currency

    @property
    def correlation_id(self) -> str:
        return f"trade:{self.trade_id}"

    @property
    def reason(self) -> str:
        return self._reason

    @property
    def status(self) -> TradeStatus:
        return self._status

    @singledispatch
    def apply(self, event):
        pass

    @apply.register(TradeCreatedEvent)
    def _(self, event: TradeCreatedEvent):
        self._trade_id = event.trade_id
        self._trader_name = event.trader_name
        self._currency_pair = event.currency_pair
        self._spot_rate = event.spot_rate
        self._trade_date = event.trade_date
        self._value_date = event.value_date
        self._direction = event.direction
        self._notional = event.notional
        self._dealt_currency = event.dealt_currency
        self._status = TradeStatus.PENDING.value

    @apply.register(TradeCompletedEvent)
    def _(self, event: TradeCompletedEvent):
        self._status = TradeStatus.DONE.value

    @apply.register(TradeRejectedEvent)
    def _(self, event: TradeRejectedEvent):
        self._status = TradeStatus.REJECTED.value
        self._reason = event.reason

    def reject(self, reason: str):
        self.raise_event(TradeRejectedEvent(trade_id=self.trade_id, reason=reason))

    def complete(self):
        self.raise_event(TradeCompletedEvent(trade_id=self.trade_id))
