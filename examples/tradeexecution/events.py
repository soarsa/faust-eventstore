from decimal import Decimal
from datetime import datetime
import uuid
from .aggregatesmeta import TradeStatus
from eventstore.event import Event


class TradeEvent(Event):
    trade_id: int


class TradeCompletedEvent(TradeEvent):
    pass

class TradeCreatedEvent(TradeEvent):

    trader_name: str
    currency_pair: str
    spot_rate: Decimal
    trade_date: datetime
    value_date: datetime
    direction: str
    notional: Decimal
    dealt_currency: str
    status: TradeStatus


class TradeRejectedEvent(TradeEvent):

    reason: str


class TradeEventFactory:

    @staticmethod
    def create_trade_created_event(trade_id: str, trader_name: str, currency_pair: str, spot_rate: Decimal,
                                   trade_date: datetime, value_date: datetime, direction: str, notional: Decimal,
                                   dealt_currency: str, status: TradeStatus):

        event_id = uuid.uuid4()

        return TradeCreatedEvent(event_id=event_id, trade_id=trade_id, trader_name=trader_name,
                                 currency_pair=currency_pair, spot_rate=spot_rate, trade_date=trade_date,
                                 value_date=value_date, direction=direction, notional=notional,
                                 dealt_currency=dealt_currency, status=status)

    @staticmethod
    def create_trade_completed_event(trade_id: str):
        event_id = uuid.uuid4()
        return TradeCompletedEvent(event_id=event_id, trade_id=trade_id)

    @staticmethod
    def create_trade_rejected_event(trade_id: str, reason: str):
        event_id = uuid.uuid4()
        return TradeRejectedEvent(event_id=event_id, trade_id=trade_id, reason=reason)
