#!/usr/bin/python3
""" LRUCache module """
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class that inherits from BaseCaching.
    Implements a caching system with an LRU
    (Least Recently Used) eviction policy.
    """

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        # List to track the access order of the keys
        self.access_order = []

    def put(self, key, item):
        """
        Add an item in the cache.

        Args:
            key: The key under which to store the item.
            item: The item to store in the cache.
        
        If either key or item is None, this method does nothing.
        If the cache exceeds its MAX_ITEMS,
        it discards the least recently used item.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                # Remove the key from the access order list to update its position
                self.access_order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Evict the least recently used item (the first item in the list)
                lru_key = self.access_order.pop(0)
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")
            
            # Add or update the key in the cache and the access order list
            self.cache_data[key] = item
            self.access_order.append(key)

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
            # Update the access order because this key was recently accessed
            self.access_order.remove(key)
            self.access_order.append(key)
            return self.cache_data.get(key)
        return None
