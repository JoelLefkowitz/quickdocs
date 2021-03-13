from inspect import Parameter, signature
from typing import Any, Set


def cls_defaults(cls: Any) -> Set[str]:
    """
    Get the set of annotations on a class that have default values.

    Args:
        cls (Any): Annotated class.

    Returns:
        Set[str]: Set of annotations.
    """
    return set(
        k
        for k, v in signature(cls.__init__).parameters.items()
        if v.default is not Parameter.empty
    )
