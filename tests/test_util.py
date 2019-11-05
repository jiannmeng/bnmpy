from util import ensure_list, to_datetime, has_tz
from datetime import datetime, timezone
from dateutil import tz

# Timezones
UTC = tz.gettz("UTC")
MYT = tz.gettz("Asia/Kuala_Lumpur")


def test_ensure_list():
    assert ensure_list("hello") == ["hello"]
    assert ensure_list(1) == [1]
    assert ensure_list({"hello": "world"}) == [{"hello": "world"}]
    assert ensure_list(["a", "b", "c"]) == ["a", "b", "c"]
    assert set(ensure_list(set(["hello", "world"]))) == set(["hello", "world"])
    assert ensure_list(None) == []
    assert ensure_list([None]) == [None]


def test_to_datetime():
    # Datetime object returned unchanged.
    assert to_datetime(datetime(2019, 6, 7)) == datetime(2019, 6, 7)

    # / in string means day-month-year format.
    assert to_datetime("07/06/2019") == datetime(2019, 6, 7)
    assert to_datetime("7/6/19") == datetime(2019, 6, 7)
    assert to_datetime("7/8/09") == datetime(2009, 8, 7)

    # - in string means year-month-day format.
    assert to_datetime("2019-06-07") == datetime(2019, 6, 7)
    assert to_datetime("2019-11-05 18:20:52") == datetime(2019, 11, 5, 18, 20, 52)

    # Otherwise, wildcard parsing.
    assert to_datetime("5 May, 2019 4:15 PM") == datetime(2019, 5, 5, 16, 15, 0)


def test_to_datetime_with_timezones():
    # Strip timezones.
    assert to_datetime(datetime(2019, 6, 7, tzinfo=UTC), tz_aware=False) == datetime(
        2019, 6, 7, 0, 0, 0
    )
    assert to_datetime(datetime(2019, 6, 7, tzinfo=MYT), tz_aware=False) == datetime(
        2019, 6, 7, 0, 0, 0
    )
    assert to_datetime("2019-11-05T12:20:52Z", tz_aware=False) == datetime(
        2019, 11, 5, 12, 20, 52
    )
    assert to_datetime("2019-11-05T12:20:52+0800", tz_aware=False) == datetime(
        2019, 11, 5, 12, 20, 52
    )
    assert to_datetime("2019-11-05T12:20:52+08:00", tz_aware=False) == datetime(
        2019, 11, 5, 12, 20, 52
    )

    # Convert to MYT (+8:00 UTC).
    assert to_datetime(datetime(2019, 6, 7, tzinfo=UTC), tz_aware=True) == datetime(
        2019, 6, 7, 8, 0, 0, tzinfo=MYT
    )
    assert to_datetime(datetime(2019, 6, 7, tzinfo=MYT), tz_aware=True) == datetime(
        2019, 6, 7, 0, 0, 0, tzinfo=MYT
    )
    assert to_datetime("2019-11-05T12:20:52Z", tz_aware=True) == datetime(
        2019, 11, 5, 20, 20, 52, tzinfo=MYT
    )
    assert to_datetime("2019-11-05T12:20:52+0800", tz_aware=True) == datetime(
        2019, 11, 5, 12, 20, 52, tzinfo=MYT
    )
    assert to_datetime("2019-11-05T12:20:52+08:00", tz_aware=True) == datetime(
        2019, 11, 5, 12, 20, 52, tzinfo=MYT
    )


def test_has_tz():
    assert not has_tz(datetime(2000, 1, 1))
    assert has_tz(datetime(2000, 1, 1, tzinfo=timezone.utc))
    assert has_tz(datetime(2000, 1, 1, tzinfo=MYT))
