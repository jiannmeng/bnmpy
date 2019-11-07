import pytest
import responses

from bnmpy import BASE_URL, Bnmpy


@pytest.fixture
def mock_basic():
    with responses.RequestsMock(assert_all_requests_are_fired=False) as r:
        r.add(
            responses.GET, BASE_URL + "none", json={"data": None}, status=200,
        )
        r.add(
            responses.GET,
            BASE_URL + "single",
            json={"data": {"hello": "world"}},
            status=200,
        )
        r.add(
            responses.GET,
            BASE_URL + "list-single",
            json={"data": [{"hello": "world"}]},
            status=200,
        )
        r.add(
            responses.GET,
            BASE_URL + "list-multi",
            json={"data": [{"hello": "world"}, {"foo": "bar"}]},
            status=200,
        )
        r.add(
            responses.GET,
            BASE_URL + "fail",
            json={"message": "No records found.", "code": 404},
            status=404,
        )
        yield r


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
