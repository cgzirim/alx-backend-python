#!/usr/bin/env python3
"""Defines the funtion sum_mixed_list."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of all floats and ints in a list."""
    return sum(mxd_lst)
