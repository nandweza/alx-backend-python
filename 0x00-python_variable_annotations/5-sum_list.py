#!/usr/bin/env python3
"""Complex types - list of floats"""

from typing import List


input_list: List[List[float]] = []


def sum_list(input_list) -> float:
    """a type-annotated function sum_list which takes a list input_list of
    floats as argument and returns their sum as a float."""
    return sum(input_list)
