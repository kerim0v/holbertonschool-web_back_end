#!/usr/bin/env python3
"""Module that creates a key-value tuple with a squared value."""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple of the string k and the square of v as a float."""
    return (k, float(v ** 2))
