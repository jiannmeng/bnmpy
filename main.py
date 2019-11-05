import requests

from util import ensure_list

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
    pass
