import requests

from util import endpoint_merge, ensure_list, to_datetime, to_strlist

BASE_URL = "https://api.bnm.gov.my/public/"
HEADERS = {"Accept": "application/vnd.BNM.API.v1+json"}


def lazy_property(fn):
    """Decorator that makes a property lazy-evaluated.

    Ref: https://stevenloria.com/lazy-properties/

    Any code which is needed to set the property is only run when first accessing
    the property. When accessing the code in the future, it retrives the cached values.
    """

    attr_name = "_lazy_" + fn.__name__

    @property
    def _lazy_property(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)

    return _lazy_property


class Bnmpy:
    """Main class which handles querying the live BNM API and storing the results.

    This is designed to be subclassed, one subclass for each API endpoint.
    e.g. "/base-rate" API endpoint is reflected as BaseRate class, which is subclass
    of BnmpyItem.

    BnmpyItem is lazy - it will only query API once you attempt to access data.
    Just doing something like `b = BnmpyItem("welcome")` will not query the API,
    but accessing `b.data` will query the API and cache the responses.

    Parameters:
    endpoints - str or list of strings. Used to form the requests made to API.

    Attributes:
    data - List of dictionaries, corresponding to the data retrieved from API. The
           data might be filtered if more data is retrieved than what is requested. For
           example, if you ask for data from dates "1/1/19" to "5/1/19", but BNM API
           responds with the whole of January's data, then only data from "1/1/19" to
           "5/1/19" can be found here.
    requests - List of request objects. The request objects are from the `requests`
               python package. The raw json responses can be found by analysing each
               request object.
    endpoints - List of endpoints. These are used to create the request objects above.
    meta - Dictionary. Contains meta information returned by BNM API. Not implemented
           yet.
    _start, _end, _filter_key -
        To be set by subclasses. If all 3 values are set, any dictionary in `data`
        whose date (represented by `_filter_key`) is before `_start` or after `_end`
        will be excluded.
    """

    def __init__(self, endpoints=None):
        self.meta = {}
        self.endpoints = ensure_list(endpoints)

    @lazy_property
    def requests(self):
        """List of request objects, one for each endpoint"""
        r = [requests.get(BASE_URL + e, headers=HEADERS) for e in self.endpoints]
        return r

    @lazy_property
    def data(self):
        """List of dicts, based on the response from BNM API."""

        # Merge all the response contents into a list of dictionaries: `data`.
        data = []
        for r in self.requests:
            if r.status_code == requests.codes.ok:
                d = ensure_list(r.json()["data"])
                data.extend(d)

        # Delete anything in data which is not between start and end dates.
        if all([hasattr(self, attr) for attr in ["_start", "_end", "_filter_key"]]):
            self._start = to_datetime(self._start)
            self._end = to_datetime(self._end)
            data = [
                entry
                for entry in data
                if self._start <= to_datetime(entry[self._filter_key]) <= self._end
            ]

        return data

    def base_rate(self, bank_code=None):
        if bank_code is None:
            self.endpoints = ["base-rate"]
        else:
            bank_code = ensure_list(bank_code)
            self.endpoints = [f"base-rate/{b}" for b in bank_code]
        return self

    def fx_turn_over(self, date=None, start=None, end=None):
        if date is None and start is None and end is None:
            self.endpoints = ["fx-turn-over"]
        elif date is not None:
            self.endpoints = endpoint_merge("fx-turn-over", to_strlist(dates=date))
        elif start is not None and end is not None:
            self._start = start
            self._end = end
            self._filter_key = "date"
            self.endpoints = endpoint_merge(
                "fx-turn-over", to_strlist(start=start, end=end, period="month")
            )
        return self

    def interbank_swap(self, date=None, start=None, end=None):
        if date is None and start is None and end is None:
            self.endpoints = ["interbank-swap"]
        elif date is not None:
            self.endpoints = endpoint_merge("interbank-swap", to_strlist(dates=date))
        elif start is not None and end is not None:
            self._start = start
            self._end = end
            self._filter_key = "date"
            self.endpoints = endpoint_merge(
                "interbank-swap", to_strlist(start=start, end=end, period="month")
            )
        return self


# class BaseRate(Bnmpy):
#     def __init__(self, bank_codes=None):
#         if bank_codes is None:
#             endpoints = "base-rate"
#         else:
#             bank_codes = ensure_list(bank_codes)
#             endpoints = [f"base-rate/{b}" for b in bank_codes]
#         super().__init__(endpoints=endpoints)


# class FxTurnOver(Bnmpy):
#     def __init__(self, date=None, start=None, end=None):
#         if date is None and start is None and end is None:
#             endpoints = "fx-turn-over"
#         elif date is not None:
#             endpoints = endpoint_merge("fx-turn-over", to_strlist(dates=date))
#         elif start is not None and end is not None:
#             self._start = start
#             self._end = end
#             self._filter_key = "date"
#             endpoints = endpoint_merge(
#                 "fx-turn-over", to_strlist(start=start, end=end, period="month")
#             )
#         super().__init__(endpoints=endpoints)


# class InterbankSwap(Bnmpy):
#     def __init__(self, date=None, start=None, end=None):
#         if date is None and start is None and end is None:
#             endpoints = "interbank-swap"
#         elif date is not None:
#             endpoints = endpoint_merge("interbank-swap", to_strlist(dates=date))
#         elif start is not None and end is not None:
#             self._start = start
#             self._end = end
#             self._filter_key = "date"
#             endpoints = endpoint_merge(
#                 "interbank-swap", to_strlist(start=start, end=end, period="month")
#             )
#         super().__init__(endpoints=endpoints)
