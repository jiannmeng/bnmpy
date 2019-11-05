import requests

from util import ensure_list

BASE_URL = "https://api.bnm.gov.my/public/"
HEADERS = {"Accept": "application/vnd.BNM.API.v1+json"}


class BnmpyItem:
    def __init__(self, endpoints):
        self.data = []
        self.meta = {}

        self._endpoints = ensure_list(endpoints)
        self._requests = [
            requests.get(BASE_URL + e, headers=HEADERS) for e in self._endpoints
        ]

        # Merge the "data" values from all of the responses into 1 dictionary.
        for r in self._requests:
            if r.status_code == requests.codes.ok:
                d = ensure_list(r.json()["data"])
                self.data.extend(d)


class BaseRate(BnmpyItem):
    def __init__(self, bank_codes=None):
        if bank_codes is None:
            endpoints = "base-rate"
        else:
            bank_codes = ensure_list(bank_codes)
            endpoints = [f"base-rate/{b}" for b in bank_codes]

        super().__init__(endpoints=endpoints)


# b = BaseRate()
# print(b.data)
# b2 = BaseRate(["BIMBMYKL"])
# print(b2.data)
