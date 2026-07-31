#!/usr/bin/env python3
"""Module for task_wait_random function."""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create an asyncio.Task for wait_random(max_delay).

    Args:
        max_delay (int): max delay to pass to wait_random.

    Returns:
        asyncio.Task: the created task.
    """
    return asyncio.create_task(wait_random(max_delay))
