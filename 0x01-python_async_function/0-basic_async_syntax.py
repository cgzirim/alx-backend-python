#!/usr/bin/env python3
"""Defines the asynchronous coroutine wait_random."""
import asyncio
import random


async def wait_random(max_delay=10):
    """Waits for a random delay between 0 and max_delay seconds before
    returning the random value.
    """
    random_int = random.uniform(0, max_delay)
    await asyncio.sleep(random_int)
    return random_int
