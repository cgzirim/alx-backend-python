#!/usr/bin/env python3
"""Defines a coroutine called async_generator."""
from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """Returns a list of 10 random numbers using async comprehensing."""
    return [i async for i in async_generator()]
