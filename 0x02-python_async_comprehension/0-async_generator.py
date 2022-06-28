#!/usr/bin/env python3
"""Async Generator"""

import asyncio
import random
from typing import Generator
from unittest import result


async def async_generator() -> Generator[float, None, None]:
    """async_generator coroutine that takes no argument
    and yields a random number between 0 and 10."""
    for i in range(10):
        yield random.random()
        await asyncio.sleep(1)
