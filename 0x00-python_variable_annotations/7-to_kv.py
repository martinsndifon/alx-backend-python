#!/usr/bin/env python3
"""ALX SE"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple of str and float"""
    v = v * v
    res: Tuple[str, float] = (k, v)
    return res
