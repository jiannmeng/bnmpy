import fixtures
from bnmpy import Bnmpy
from datetime import datetime

mock_fx_turn_over = fixtures.mock_fx_turn_over


class TestFxTurnOver:
    def test_latest(self, mock_fx_turn_over):
        fto = Bnmpy().fx_turn_over()
        assert fto.endpoints == ["fx-turn-over"]
        assert len(fto.data) == 1
        assert all([k in fto.data[0] for k in ["date", "total_sum"]])

    def test_date_single(self, mock_fx_turn_over):
        fto = Bnmpy().fx_turn_over(date=datetime(2019, 1, 2))
        assert fto.endpoints == ["fx-turn-over/date/2019-01-02"]
        assert len(fto.data) == 1

    def test_date_multi(self, mock_fx_turn_over):
        fto = Bnmpy().fx_turn_over(date=[datetime(2019, 1, 2), datetime(2019, 1, 3)])
        assert fto.endpoints == [
            "fx-turn-over/date/2019-01-02",
            "fx-turn-over/date/2019-01-03",
        ]
        assert len(fto.data) == 2

    def test_range_within_month(self, mock_fx_turn_over):
        fto = Bnmpy().fx_turn_over(start=datetime(2019, 1, 2), end=datetime(2019, 1, 4))
        assert fto.endpoints == ["fx-turn-over/year/2019/month/01"]
        assert len(fto.data) == 3

    def test_range_across_months(self, mock_fx_turn_over):
        fto = Bnmpy().fx_turn_over(
            start=datetime(2019, 1, 29), end=datetime(2019, 2, 4)
        )
        assert fto.endpoints == [
            "fx-turn-over/year/2019/month/01",
            "fx-turn-over/year/2019/month/02",
        ]
        assert len(fto.data) == 4
