#!/usr/bin/env python3
"""ALX SE"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int):
    """create multiple async coroutines"""
    res = await asyncio.gather(*(wait_random(max_delay) for i in range(n)))
    return res
