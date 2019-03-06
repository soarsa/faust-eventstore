from faust import Record as FaustRecord


class Event(FaustRecord, abstract=True, isodates=True, decimals=True, serializer='json'):

    event_id: str

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)
