from typing import Dict


def merge_dicts(*args: Dict) -> Dict: 
    out = {}
    for dct in args:
        dict(out, **dct)    
    return out