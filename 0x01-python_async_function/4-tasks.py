#!/usr/bin/env python3
"""Defines the asynchronous coroutine wait_n()."""
import asyncio
import queue
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times with the specified max_delay.
    Return list of delay values.
    """
    array = []
    queue = []
    for i in range(n):
        task = task_wait_random(max_delay)
        task.add_done_callback(lambda x: array.append(x.result()))
        queue.append(task)

    for task in queue:
        await task
    
    return array
