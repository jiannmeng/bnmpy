import requests

from util import endpoint_merge, ensure_list, to_datetime, to_strlist

BASE_URL = "https://api.bnm.gov.my/public/"
HEADERS = {"Accept": "application/vnd.BNM.API.v1+json"}


def lazy_property(fn):
    """Decorator that makes a property lazy-evaluated.
    """
    # Ref: https://stevenloria.com/lazy-properties/
    attr_name = "_lazy_" + fn.__name__

    @property
    def _lazy_property(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)

    return _lazy_property


class BnmpyItem:
    def __init__(self, endpoints):
        self.meta = {}
        self.endpoints = ensure_list(endpoints)

    @lazy_property
    def requests(self):
        """List of request objects, one for each endpoint"""
        r = [requests.get(BASE_URL + e, headers=HEADERS) for e in self.endpoints]
        return r

    @lazy_property
    def data(self):
        """Merge the `data` values from all of the responses into 1 dictionary."""
        data = []
        for r in self.requests:
            if r.status_code == requests.codes.ok:
                d = ensure_list(r.json()["data"])
                data.extend(d)

        if all(
            [hasattr(self, "start"), hasattr(self, "end"), hasattr(self, "filter_key")]
        ):
            # Delete anything in data which is not between start and end dates.
            self.start = to_datetime(self.start)
            self.end = to_datetime(self.end)

            data = [
                entry
                for entry in data
                if self.start <= to_datetime(entry[self.filter_key]) <= self.end
            ]

        return data


class BaseRate(BnmpyItem):
    def __init__(self, bank_codes=None):
        if bank_codes is None:
            endpoints = "base-rate"
        else:
            bank_codes = ensure_list(bank_codes)
            endpoints = [f"base-rate/{b}" for b in bank_codes]

        super().__init__(endpoints=endpoints)


class FxTurnOver(BnmpyItem):
    def __init__(self, dates=None, start=None, end=None):
        if dates is None and start is None and end is None:
            endpoints = "fx-turn-over"
        elif dates is not None:
            endpoints = endpoint_merge("fx-turn-over", to_strlist(dates=dates))
        elif start is not None and end is not None:
            self.start = start
            self.end = end
            self.filter_key = "date"
            endpoints = endpoint_merge(
                "fx-turn-over", to_strlist(start=start, end=end, period="month")
            )

        super().__init__(endpoints=endpoints)
