#!/usr/bin/env python3
"""ALX SE"""
async_generator = __import__('0-async_generator').async_generator
from typing import List


async def async_comprehension() -> List[float]:
    """Compute using asynchronous list comprehension"""
    return [i async for i in async_generator()]
