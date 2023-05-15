#!/usr/bin/env python3
"""Script hosting a auxiliary paginating function"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Takes Two Integers.
    Returns Tuple of size two containing a start Index
    and End Index corresponding to range of indices
    to return in a list for these pagination params"""

    if page > 0:
        if page == 1:
            start_index = 0
            end_index = page_size

        else:
            end_index = page * page_size
            start_index = end_index - page_size

    return start_index, end_index
