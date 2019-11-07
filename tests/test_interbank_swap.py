from datetime import datetime

import fixtures
from bnmpy import Bnmpy

mock_interbank_swap = fixtures.mock_interbank_swap


class TestInterbankSwap:
    def test_latest(self, mock_interbank_swap):
        fto = Bnmpy().interbank_swap()
        assert fto.endpoints == ["interbank-swap"]
        assert len(fto.data) == 1
        assert all(
            [
                k in fto.data[0]
                for k in [
                    "date",
                    "overnight",
                    "1_week",
                    "2_week",
                    "1_month",
                    "2_month",
                    "3_month",
                    "6_month",
                    "9_month",
                    "12_month",
                    "more_1_year",
                ]
            ]
        )

    def test_date_single(self, mock_interbank_swap):
        fto = Bnmpy().interbank_swap(date=datetime(2019, 1, 2))
        assert fto.endpoints == ["interbank-swap/date/2019-01-02"]
        assert len(fto.data) == 1

    def test_date_multi(self, mock_interbank_swap):
        fto = Bnmpy().interbank_swap(date=[datetime(2019, 1, 2), datetime(2019, 1, 3)])
        assert fto.endpoints == [
            "interbank-swap/date/2019-01-02",
            "interbank-swap/date/2019-01-03",
        ]
        assert len(fto.data) == 2

    def test_range_within_month(self, mock_interbank_swap):
        fto = Bnmpy().interbank_swap(
            start=datetime(2019, 1, 2), end=datetime(2019, 1, 4)
        )
        assert fto.endpoints == ["interbank-swap/year/2019/month/01"]
        assert len(fto.data) == 3

    def test_range_across_months(self, mock_interbank_swap):
        fto = Bnmpy().interbank_swap(
            start=datetime(2019, 1, 29), end=datetime(2019, 2, 4)
        )
        assert fto.endpoints == [
            "interbank-swap/year/2019/month/01",
            "interbank-swap/year/2019/month/02",
        ]
        assert len(fto.data) == 4
