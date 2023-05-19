#!/usr/bin/python3
"""Implementation of the FIFO Caching Policy"""


from typing import Any
BasicCache = __import__('0-basic_cache').BasicCache


class FIFOCache(BasicCache):
    """A Class That Inherits from the `BaseCache` Class
    It is A Caching System Implementing FIFO Policy
    """

    def __init__(self) -> None:
        """Initializes using parent class Init"""

        super().__init__()

    def put(self, key: Any, item: Any) -> None:
        """ Adding an Item into the caching system
        This FIFO function relies on insertion order
        preservation which is guaranteed in Python 3.7 +"""

        if key is None or item is None:
            return

        if key in self.cache_data:
            super().put(key, item)
            super().print_cache()

        if len(self.cache_data) == super().MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            del self.cache_data[first_key]

            super().put(key, item)
            print('DISCARD: {}'.format(first_key))

        super().put(key, item)

    def get(self, key: Any) -> Any:
        """Returns the Value Associated with Key in `self.cache_data`"""

        return super().get(key)
