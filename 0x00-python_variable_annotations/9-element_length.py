#!/usr/bin/env python3
"""module 9"""


from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns values with the appropriate types"""
    return [(i, len(i)) for i in lst]
