#!/usr/bin/python3
""" MRUCache module """
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class that inherits from BaseCaching.
    Implements a caching system with an MRU
    (Most Recently Used) eviction policy.
    """

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        # To keep track of the most recently used key
        self.most_recent_key = None

    def put(self, key, item):
        """
        Add an item in the cache.

        Args:
            key: The key under which to store the item.
            item: The item to store in the cache.

        If either key or item is None, this method does nothing.
        If the cache exceeds its MAX_ITEMS,
        it discards the most recently used item.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                # Just update the value; the key remains the most recent
                self.cache_data[key] = item
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    # Evict the most recently used item
                    if self.most_recent_key is not None:
                        del self.cache_data[self.most_recent_key]
                        print(f"DISCARD: {self.most_recent_key}")

                # Add the new key-value pair to the cache
                self.cache_data[key] = item

            # Update the most recent key
            self.most_recent_key = key

    def get(self, key):
        """
        Get an item by key.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The value associated with the key, or None if the key is None
            or does not exist in the cache.
        """
        if key is not None and key in self.cache_data:
            # Update the most recent key because this key was just accessed
            self.most_recent_key = key
            return self.cache_data.get(key)
        return None
