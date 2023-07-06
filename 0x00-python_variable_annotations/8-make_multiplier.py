#!/usr/bin/env python3
"""ALX SE"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a callable function"""
    def fn(multiplier2: float) -> float:
        """Multiplies the main multiplier"""
        return multiplier * multiplier2
    return fn
