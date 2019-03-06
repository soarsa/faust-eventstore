import uuid
from datetime import datetime, timedelta
import asyncio
from eventstore.repository import Repository
from examples.tradeexecution.aggregates import Trade
from examples.tradeexecution.mocker import create_dummy_trade_request


async def async_main():

    request = create_dummy_trade_request()
    trade_id = str(uuid.uuid4())
    trade_date = datetime.now() + timedelta(days=2)

    trade = Trade(trade_id, request.trader_name, request.currency_pair, request.spot_rate, trade_date,
                  request.value_date, request.direction, request.notional, request.dealt_currency)

    repository = Repository()
    result = await repository.add(trade.correlation_id, trade)
    print(result)
    exists = await repository.exists(trade.correlation_id)
    print(exists)
    retrieved = await repository.get(trade.correlation_id)
    print(retrieved)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_main())
