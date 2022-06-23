#!/usr/bin/env python3
"""Defines the function to_kv."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tupple of str and float."""
    return (k, v**2)
