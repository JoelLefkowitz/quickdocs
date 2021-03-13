from typing import Any, Dict

AnyDict = Dict[Any, Any]


def merge_dicts(*args: AnyDict) -> Dict:
    """
    Successively merge any number of dictionaries.

    >>> merge_dicts({'a': 1}, {'b': 2})
    {'a': 1, 'b': 2}

    >>> merge_dicts({'a': 1}, {'a': 2}, {'a': 3})
    {'a': 3}

    Returns:
        Dict: Dictionary of merged inputs.
    """
    out = {}  # type: AnyDict
    for dct in args:
        out = {**out, **dct}
    return out
