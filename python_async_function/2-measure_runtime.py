#!/usr/bin/env python3
"""Module for measure_time function."""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """Measure the average time per call of wait_n(n, max_delay).

    Args:
        n (int): number of coroutines to spawn.
        max_delay (int): max delay for each coroutine.

    Returns:
        float: total_time / n
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time

    return total_time / n
