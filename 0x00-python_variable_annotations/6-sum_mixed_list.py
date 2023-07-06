#!/usr/bin/env python3
"""ALX SE"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Returns sum of numbers in a list"""
    return sum(x for x in mxd_list)
