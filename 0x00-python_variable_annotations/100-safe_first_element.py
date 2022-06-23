#!/usr/bin/env python3
"""module 10"""


from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Retrieves first element of a sequence if it exists."""
    if lst:
        return lst[0]
    else:
        return None
