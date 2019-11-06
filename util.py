from datetime import datetime, timedelta
from typing import List, Optional, Set, Tuple, Union

from dateparser import parse
from dateutil import tz
from dateutil.parser import ParserError


def ensure_list(s: Optional[Union[str, List[str], Tuple[str], Set[str]]]) -> List[str]:
    # Ref: https://stackoverflow.com/a/56641168/
    return (
        s
        if isinstance(s, list)
        else list(s)
        if isinstance(s, (tuple, set))
        else []
        if s is None
        else [s]
    )


def to_datetime(s, tz_aware=False):
    output = None
    if isinstance(s, datetime):
        output = s
    elif "-" in s:
        output = parse(s, settings={"DATE_ORDER": "YMD"})
    elif "/" in s:
        output = parse(s, settings={"DATE_ORDER": "DMY"})
    else:
        output = parse(s)

    if output is None:
        raise ParserError(
            "When entering a date, please use a datetime object, 'dd/mm/yyyy' string format, or 'yyyy-mm-dd' string format."
        )

    if tz_aware:
        MYT = tz.gettz("Asia/Kuala_Lumpur")  # Malaysia timezone.
        output = (
            output.astimezone(MYT) if has_tz(output) else output.replace(tzinfo=MYT)
        )
    else:
        output = output.replace(tzinfo=None)

    return output


def has_tz(dt):
    """Returns True if datetime is timezone aware, and false otherwise."""
    # Ref: https://stackoverflow.com/a/50710825
    return dt.tzinfo is not None and dt.tzinfo.utcoffset(dt) is not None


def to_strlist(dates=None, start=None, end=None, period="day"):
    if dates is None:
        start = to_datetime(start, tz_aware=False).replace(
            hour=0, minute=0, second=0, microsecond=0
        )
        end = to_datetime(end, tz_aware=False).replace(
            hour=0, minute=0, second=0, microsecond=0
        )

        if start > end:
            start, end = end, start

        dates = [start + timedelta(days=x) for x in range((end - start).days + 1)]
    else:
        dates = [to_datetime(dt) for dt in ensure_list(dates)]

    if period == "day":
        output = [dt.strftime("date/%Y-%m-%d") for dt in dates]  # "2019-01-01"
    elif period == "month":
        dates = [dt.replace(day=1) for dt in dates]
        dates = list(set(dates))  # Remove duplicate months.
        dates.sort()
        output = [
            dt.strftime("year/%Y/month/%m") for dt in dates
        ]  # "year/2019/month/1"
    elif period == "year":
        dates = [dt.replace(month=1, day=1) for dt in dates]
        dates = list(set(dates))  # Remove duplicate years.
        dates.sort()
        output = [dt.strftime("year/%Y") for dt in dates]  # "year/2019"
    else:
        raise ValueError("period must be 'day', 'month' or 'year'")

    return output


def endpoint_merge(s1, s2):
    s1 = ensure_list(s1)
    s2 = ensure_list(s2)
    return [f"{x}/{y}" for x in s1 for y in s2]
