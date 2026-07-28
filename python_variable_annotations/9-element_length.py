#!/usr/bin/env python3
"""Module that annotates element_length."""
from typing import List, Sequence, Tuple


def element_length(lst: List[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples with each element and its length."""
    return [(i, len(i)) for i in lst]
