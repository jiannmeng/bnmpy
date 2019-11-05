from datetime import datetime
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
