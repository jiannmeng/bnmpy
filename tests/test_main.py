import responses
import pytest

from main import BnmpyItem, BASE_URL


@pytest.fixture
def mock_responses():
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


def test_single(mock_responses):
    b = BnmpyItem("single")
    assert b.data == [{"hello": "world"}]


def test_list_single(mock_responses):
    b = BnmpyItem("list-single")
    assert b.data == [{"hello": "world"}]


def test_list_multi(mock_responses):
    b = BnmpyItem("list-multi")
    assert b.data == [{"hello": "world"}, {"foo": "bar"}]


def test_none(mock_responses):
    b = BnmpyItem("none")
    assert b.data == []


def test_list_combine(mock_responses):
    b = BnmpyItem(["none", "single", "list-single", "list-multi", "fail"])
    assert b.data == [
        {"hello": "world"},
        {"hello": "world"},
        {"hello": "world"},
        {"foo": "bar"},
    ]
