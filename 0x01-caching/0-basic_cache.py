#!/usr/bin/python3
"""Implementation of the `BasicCache` Class"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """A Caching System Class that inherits from `BaseCaching`.
    """

    def __init__(self):
        """Initialization Inherited from parent class"""

        super().__init__()

    def put(self, key, item):
        """Adds An Item in the Cache Dictionary `cache` data"""

        self.cache_data[key] = item

    def get(self, key):
        """Get an Item by Key"""

        return self.cache_data.get(key, None)
