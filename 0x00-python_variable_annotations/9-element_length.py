#!/usr/bin/env python3
"""ALX SE"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples of sequence and integer"""
    return [(i, len(i)) for i in lst]
