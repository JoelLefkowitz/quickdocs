from inspect import Parameter, signature
from typing import Any, Set


def cls_defaults(cls: Any) -> Set[str]:
    return set(
        k
        for k, v in signature(cls.__init__).parameters.items()
        if v.default is not Parameter.empty
    )
