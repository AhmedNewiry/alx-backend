#!/usr/bin/python3
""" BasicCache module """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class that inherits from BaseCaching.
    This caching system has no limit on the number of items stored.
    """

    def put(self, key, item):
        """
        Add an item in the cache.

        Args:
            key: The key under which to store the item.
            item: The item to store in the cache.
        
        If either key or item is None, this method does nothing.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key.

        Args:
            key: The key of the item to retrieve.
        
        Returns:
            The value associated with the key, or None if the key is None
            or does not exist in the cache.
        """
        return self.cache_data.get(key, None)
