#!/usr/bin/env python3
"""ALX SE"""
from typing import Iterator
import asyncio
import random


async def async_generator() -> Iterator[float]:
    """Generate an iterator"""
    for i in range(10):
        ran = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield ran
