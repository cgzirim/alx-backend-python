#!/usr/bin/env python3
"""Defines the function make_multiplier."""
from audioop import mul
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier."""
    def product(f: float):
        return f * multiplier

    return product