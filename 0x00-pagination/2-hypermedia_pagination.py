#!/usr/bin/env python3
"""Script of Implementation of a Simple
    and Hypermedia Pagination"""

import csv
import math
from typing import List, Tuple, Optional, Union


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


class Server:

    """Server class to paginate a database of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """A Method that returns Paginated dataset entries based on the
        page no and page_size params.
        """

        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.dataset()
        start_index, end_index = index_range(page, page_size)

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """A Method that implements Hypermedia pagination
        takes `page` and `page_size` as params with default values.
        Returns a dictionary with key value pairs."""

        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
                "page_size": len(dataset),
                "page": page,
                "data": dataset,
                "next_page": next_page,
                "prev_page": prev_page,
                "total_pages": total_pages
                }
