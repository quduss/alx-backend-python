#!/usr/bin/env python3
"""multiple coroutines module"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """execute multiple coroutines"""
    tasks = []
    for i in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)
    tasks = tuple(tasks)
    results = await asyncio.gather(*tasks)
    return sorted(results)
