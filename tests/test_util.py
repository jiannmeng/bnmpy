from util import ensure_list


def test_ensure_list():
    assert ensure_list("hello") == ["hello"]
    assert ensure_list(1) == [1]
    assert ensure_list({"hello": "world"}) == [{"hello": "world"}]
    assert ensure_list(["a", "b", "c"]) == ["a", "b", "c"]
    assert set(ensure_list(set(["hello", "world"]))) == set(["hello", "world"])
    assert ensure_list(None) == []
    assert ensure_list([None]) == [None]
