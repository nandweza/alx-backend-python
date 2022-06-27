#!/usr/bin/env python3
"""module 4"""

import asyncio
import random
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    return the list of all the delays(float values).
    """
    queue, array = [], []

    for i in range(n):
        task_delay = task_wait_random(max_delay)
        task_delay.add_done_callback(lambda x: array.append(x.result()))
        queue.append(task_delay)

    for q in queue:
        await q

    return array
