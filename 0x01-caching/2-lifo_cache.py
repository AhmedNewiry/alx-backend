#!/usr/bin/python3
""" LIFOCache module """

from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """
    LIFOCache class that inherits from BaseCaching.
    Implements a caching system with a LIFO
    (Last-In-First-Out) eviction policy.
    """

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """
        Add an item in the cache.

        Args:
            key: The key under which to store the item.
            item: The item to store in the cache.
        
        If either key or item is None,
        this method does nothing.
        If the cache exceeds its MAX_ITEMS,
        it discards the last item added to the cache.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                # Remove the key from the stack if it
                #already exists (to update its position)
                self.stack.remove(key)
            self.cache_data[key] = item
            self.stack.append(key)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Evict the last item in the stack (LIFO)
                last_key = self.stack.pop(-2)
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")

    def get(self, key):
        """
        Get an item by key.

        Args:
            key: The key of the item to retrieve.
        
        Returns:
            The value associated with the key,
            or None if the key is None
            or does not exist in the cache.
        """
        return self.cache_data.get(key, None)
