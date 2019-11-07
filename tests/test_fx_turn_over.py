from datetime import datetime

import pytest
import responses

from bnmpy import BASE_URL, FxTurnOver


@pytest.fixture
def mock_fx_turn_over():
    with responses.RequestsMock(assert_all_requests_are_fired=False) as r:
        r.add(
            responses.GET,
            BASE_URL + "fx-turn-over",
            json={
                "data": {"date": "2019-11-04", "total_sum": 10.08},
                "meta": {"last_updated": "2019-11-04 07:00:06", "total_result": 1},
            },
            status=200,
        )
        r.add(
            responses.GET,
            BASE_URL + "fx-turn-over/date/2019-01-02",
            json={
                "data": {"date": "2019-01-02", "total_sum": 11.7},
                "meta": {"last_updated": "2019-11-04 07:00:06", "total_result": 1},
            },
            status=200,
        )
        r.add(
            responses.GET,
            BASE_URL + "fx-turn-over/date/2019-01-03",
            json={
                "data": {"date": "2019-01-03", "total_sum": 12.93},
                "meta": {"last_updated": "2019-11-04 07:00:06", "total_result": 1},
            },
            status=200,
        )
        r.add(
            responses.GET,
            BASE_URL + "fx-turn-over/date/2019-01-04",
            json={
                "data": {"date": "2019-01-04", "total_sum": 12.88},
                "meta": {"last_updated": "2019-11-04 07:00:06", "total_result": 1},
            },
            status=200,
        )
        r.add(
            responses.GET,
            BASE_URL + "fx-turn-over/year/2019/month/01",
            json={
                "data": [
                    {"date": "2019-01-31", "total_sum": 14.17},
                    {"date": "2019-01-30", "total_sum": 11.7},
                    {"date": "2019-01-29", "total_sum": 12.68},
                    {"date": "2019-01-28", "total_sum": 10.4},
                    {"date": "2019-01-25", "total_sum": 15.23},
                    {"date": "2019-01-24", "total_sum": 13.67},
                    {"date": "2019-01-23", "total_sum": 13.73},
                    {"date": "2019-01-22", "total_sum": 16.57},
                    {"date": "2019-01-18", "total_sum": 12.84},
                    {"date": "2019-01-17", "total_sum": 14.26},
                    {"date": "2019-01-16", "total_sum": 12.57},
                    {"date": "2019-01-15", "total_sum": 12.18},
                    {"date": "2019-01-14", "total_sum": 13.75},
                    {"date": "2019-01-11", "total_sum": 12.46},
                    {"date": "2019-01-10", "total_sum": 13.02},
                    {"date": "2019-01-09", "total_sum": 13.49},
                    {"date": "2019-01-08", "total_sum": 11.45},
                    {"date": "2019-01-07", "total_sum": 14.28},
                    {"date": "2019-01-04", "total_sum": 12.88},
                    {"date": "2019-01-03", "total_sum": 12.93},
                    {"date": "2019-01-02", "total_sum": 11.7},
                ],
                "meta": {"last_updated": "2019-11-04 07:00:06", "total_result": 21},
            },
            status=200,
        )
        r.add(
            responses.GET,
            BASE_URL + "fx-turn-over/year/2019/month/02",
            json={
                "data": [
                    {"date": "2019-02-28", "total_sum": 12.84},
                    {"date": "2019-02-27", "total_sum": 13.71},
                    {"date": "2019-02-26", "total_sum": 13.39},
                    {"date": "2019-02-25", "total_sum": 11.21},
                    {"date": "2019-02-22", "total_sum": 12.87},
                    {"date": "2019-02-21", "total_sum": 13.05},
                    {"date": "2019-02-20", "total_sum": 13.55},
                    {"date": "2019-02-19", "total_sum": 11.54},
                    {"date": "2019-02-18", "total_sum": 6.01},
                    {"date": "2019-02-15", "total_sum": 10.25},
                    {"date": "2019-02-14", "total_sum": 12.83},
                    {"date": "2019-02-13", "total_sum": 11.71},
                    {"date": "2019-02-12", "total_sum": 12.87},
                    {"date": "2019-02-11", "total_sum": 11.68},
                    {"date": "2019-02-08", "total_sum": 10.79},
                    {"date": "2019-02-07", "total_sum": 11.37},
                    {"date": "2019-02-04", "total_sum": 10.69},
                ],
                "meta": {"last_updated": "2019-11-04 07:00:06", "total_result": 17},
            },
            status=200,
        )
        yield r


class TestFxTurnOver:
    def test_latest(self, mock_fx_turn_over):
        fto = FxTurnOver()
        assert fto.endpoints == ["fx-turn-over"]
        assert len(fto.data) == 1
        assert all([k in fto.data[0] for k in ["date", "total_sum"]])

    def test_date_single(self, mock_fx_turn_over):
        fto = FxTurnOver(dates=datetime(2019, 1, 2))
        assert fto.endpoints == ["fx-turn-over/date/2019-01-02"]
        assert len(fto.data) == 1

    def test_date_multi(self, mock_fx_turn_over):
        fto = FxTurnOver(dates=[datetime(2019, 1, 2), datetime(2019, 1, 3)])
        assert fto.endpoints == [
            "fx-turn-over/date/2019-01-02",
            "fx-turn-over/date/2019-01-03",
        ]
        assert len(fto.data) == 2

    def test_range_within_month(self, mock_fx_turn_over):
        fto = FxTurnOver(start=datetime(2019, 1, 2), end=datetime(2019, 1, 4))
        assert fto.endpoints == ["fx-turn-over/year/2019/month/01"]
        assert len(fto.data) == 3

    def test_range_across_months(self, mock_fx_turn_over):
        fto = FxTurnOver(start=datetime(2019, 1, 29), end=datetime(2019, 2, 4))
        assert fto.endpoints == [
            "fx-turn-over/year/2019/month/01",
            "fx-turn-over/year/2019/month/02",
        ]
        assert len(fto.data) == 4
