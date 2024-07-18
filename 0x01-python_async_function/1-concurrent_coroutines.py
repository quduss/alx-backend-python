#!/usr/bin/env python3
"""multiple coroutines module"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """execute multiple coroutines"""
    tasks = []
    for i in range(n):
        task = wait_random(max_delay)
        tasks.append(task)
    tasks = tuple(tasks)
    results = await asyncio.gather(*tasks)
    return sorted(results)
