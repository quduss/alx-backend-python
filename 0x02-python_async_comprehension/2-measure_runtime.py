#!/usr/bin/env python3
"""Task 2"""
import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure run time for four parallel comprehensions"""
    res = []
    for i in range(4):
        task = async_comprehension()
        res.append(task)
    start_time = time.time()
    result = await asyncio.gather(*res)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time
