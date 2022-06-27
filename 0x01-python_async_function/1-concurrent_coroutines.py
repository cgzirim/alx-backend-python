#!/usr/bin/env python3
"""Defines the asynchronous coroutine wait_n()."""
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """Spawn wait_random n times with the specified max_delay."""
    return [await wait_random(max_delay) for i in range(n)]