#!/usr/bin/env python3
"""Module for task_wait_n function."""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Spawn task_wait_random n times with the given max_delay.

    Args:
        n (int): number of times to spawn task_wait_random.
        max_delay (int): max delay to pass to each task_wait_random call.

    Returns:
        List[float]: delays in ascending order.
    """
    delays = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
