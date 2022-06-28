#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""

import asyncio
import timeit

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """execute async_comprehension four times in parallel
    using asyncio.gather, measures & return total runtime.
    """
    start = timeit.default_timer()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
        )
    stop = timeit.default_timer()
    return stop - start
