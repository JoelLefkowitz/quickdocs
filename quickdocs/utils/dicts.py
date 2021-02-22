from typing import Any, Dict

AnyDict = Dict[Any, Any]


def merge_dicts(*args: AnyDict) -> Dict:
    out = {}  # type: AnyDict
    for dct in args:
        out = dict(**out, **dct)
    return out
