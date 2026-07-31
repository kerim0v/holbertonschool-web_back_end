#!/usr/bin/env python3
"""Module for wait_n coroutine."""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait.random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """sadasd"""
    delays = []
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
