#!/usr/bin/env python3
"""ALX SE"""
from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return an element from the sequence or None"""
    if lst:
        return lst[0]
    else:
        return None
