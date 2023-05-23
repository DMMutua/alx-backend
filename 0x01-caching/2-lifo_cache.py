#!/usr/bin/python3
"""Implementing A Cache Engine with LIFO Protocol"""


from typing import Any
BasicCache = __import__('0-basic_cache').BasicCache


class LIFOCache(BaseCaching):
    """Caching Engine with LIFO protocol"""

    def __init__(self) -> None:
        """Instanciating Cache dictionary"""

        super().__init__()

    def put(self, key: Any, item: Any) -> None:
        """Assigns to cache dict the item with value for Key.
        Ensures that cache is within limit by LIFO Means.
        Relies on insertion order [3.7 +]"""

        if key is None and item is None:
            return

        if key in self.cache_data:
            super().put(key, item)
            super().print_cache()

        if len(self.cache_data) == super().MAX_ITEMS:
            ejected_key, eV = self.cache_data.popitem()
            
            super().put(key, item)
            print('DISCARD: {}'.format(ejected_key))

        super().put(key, item)

    def get(self, key: Any) -> Any:
        """Returns the value in Cache linked to key"""

        return super().get(key)
