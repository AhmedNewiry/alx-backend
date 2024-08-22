#!/usr/bin/python3
""" LFUCache module """

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache class that inherits from BaseCaching.
    Implements a caching system with an LFU (Least Frequently Used)
    eviction policy.
    """

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.frequency = {}  # To keep track of the frequency of each key
        self.usage_order = {}  # To keep track of the order of usage

    def put(self, key, item):
        """
        Add an item in the cache.

        Args:
            key: The key under which to store the item.
            item: The item to store in the cache.

        If either key or item is None, this method does nothing.
        If the cache exceeds its MAX_ITEMS, it discards the least frequently
        used item. In case of a tie in frequency, it uses the LRU (Least
        Recently Used) policy.
        """
        if key is not None and item is not None:
            if (len(self.cache_data) >= BaseCaching.MAX_ITEMS and
                    key not in self.cache_data):
                # Find the least frequently used keys
                min_freq = min(self.frequency.values())
                least_freq_keys = [
                    k for k, v in self.frequency.items() if v == min_freq]

                # Resolve ties by least recently used policy
                if len(least_freq_keys) > 1:
                    oldest_key = min(
                        least_freq_keys, key=lambda k: self.usage_order[k])
                else:
                    oldest_key = least_freq_keys[0]

                # Evict the chosen key
                del self.cache_data[oldest_key]
                del self.frequency[oldest_key]
                del self.usage_order[oldest_key]
                print(f"DISCARD: {oldest_key}")

            # Add/Update the cache data
            self.cache_data[key] = item

            # Update frequency and usage order
            if key in self.frequency:
                self.frequency[key] += 1
            else:
                self.frequency[key] = 1

            # Update the usage order to reflect the most recent use
            self.usage_order[key] = len(self.usage_order)

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
            # Increase the frequency since the key is being accessed
            self.frequency[key] += 1
            # Update the usage order to reflect the most recent access
            self.usage_order[key] = len(self.usage_order)
            return self.cache_data.get(key)
        return None
