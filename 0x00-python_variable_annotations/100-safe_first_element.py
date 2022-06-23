#!/usr/bin/env python3
"""Defines the function safe_first_element."""
from types import NoneType
from typing import Union, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, NoneType]:
    if lst:
        return lst[0]
    else:
        return None