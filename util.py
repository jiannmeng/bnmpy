from typing import List, Optional, Set, Tuple, Union


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
