#!/usr/bin/env python3
"""ALX SE"""
from typing import Mapping, Union, Any, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Return a value from a dictionary if true or default"""
    if key in dct:
        return dct[key]
    else:
        return default
