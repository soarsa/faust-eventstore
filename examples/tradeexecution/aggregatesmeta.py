from enum import Enum

class TradeStatus(Enum):

    PENDING = "PENDING",
    DONE = "DONE",
    REJECTED = "REJECTED"