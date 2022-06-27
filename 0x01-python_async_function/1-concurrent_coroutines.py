#!/usr/bin/env python3
"""Defines the asynchronous coroutine wait_n()."""
import asyncio
from typing import List
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times with the specified max_delay.
    Return list of delay values.
    """
    return [await wait_random(max_delay) for i in range(n)]
