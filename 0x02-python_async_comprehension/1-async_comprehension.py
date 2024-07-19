#!/usr/bin/env python3
"""Task 1"""

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """return list of 10 random numbers using an async comprehensing
    over async_generator"""
    result = []
    async for i in async_generator():
        result.append(i)
    return result
