#!/usr/bin/env python3
"""Defines the function safe_first_element."""
from typing import Union, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns the first element of a sequence if it exists."""
    if lst:
        return lst[0]
    else:
        return None
