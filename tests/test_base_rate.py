import fixtures
from bnmpy import Bnmpy

mock_base_rate = fixtures.mock_base_rate


class TestBaseRate:
    def test_latest(self, mock_base_rate):
        br = Bnmpy().base_rate()
        assert br.endpoints == ["base-rate"]
        assert len(br.data) == 35
        assert all(
            [
                k in br.data[0]
                for k in [
                    "bank_code",
                    "bank_name",
                    "base_rate",
                    "base_lending_rate",
                    "indicative_eff_lending_rate",
                ]
            ]
        )

    def test_single(self, mock_base_rate):
        br = Bnmpy().base_rate("MBBEMYKL")
        assert br.endpoints == ["base-rate/MBBEMYKL"]
        assert len(br.data) == 1

    def test_multi(self, mock_base_rate):
        br = Bnmpy().base_rate(["MBBEMYKL", "CIBBMYKL"])
        assert br.endpoints == ["base-rate/MBBEMYKL", "base-rate/CIBBMYKL"]
        assert len(br.data) == 2
