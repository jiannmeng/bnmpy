import fixtures
from bnmpy import Bnmpy

mock_basic = fixtures.mock_basic


class TestBnmpyCore:
    def test_data_single(self, mock_basic):
        b = Bnmpy("single")
        assert b.data == [{"hello": "world"}]

    def test_data_list_single(self, mock_basic):
        b = Bnmpy("list-single")
        assert b.data == [{"hello": "world"}]

    def test_data_list_multi(self, mock_basic):
        b = Bnmpy("list-multi")
        assert b.data == [{"hello": "world"}, {"foo": "bar"}]

    def test_data_none(self, mock_basic):
        b = Bnmpy("none")
        assert b.data == []

    def test_data_list_combine(self, mock_basic):
        b = Bnmpy(["none", "single", "list-single", "list-multi", "fail"])
        assert b.data == [
            {"hello": "world"},
            {"hello": "world"},
            {"hello": "world"},
            {"foo": "bar"},
        ]
