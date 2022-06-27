#!/usr/bin/env python3
"""Defines the function measure_time."""
import time
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, maxdelay: int) -> float:
    """Measures the total execution time for wait_n(n, max_delay)."""
    start_time = time.perf_counter()
    wait_n(n, maxdelay)
    return time.perf_counter() - start_time
