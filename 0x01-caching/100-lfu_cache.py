#!/usr/bin/env python3
"""
LFU Cache
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    Least Frequently Used (LFU) caching system implementation.
    """
    def __init__(self):
        """
        Initialize an LFUCache instance
        """
        super().__init__()
        self.cache_order = []
        self.frequency = {}

    def put(self, key, item):
        """
        Add an item to the cache. If the cache exceeds the maximum
        size, the least frequently used item will be discarded.
        Args:
            key: The key of the item to add.
            item: The item to add to the cache.
        """
        if not key or not item:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the least frequently used key
                min_freq = min(self.frequency.values())
                lfu_keys = [k for k in
                            self.cache_order if self.frequency[k] == min_freq]
                lfu_key = lfu_keys[0]
                self.cache_order.remove(lfu_key)
                del self.cache_data[lfu_key]
                del self.frequency[lfu_key]
                print(f"DISCARD: {lfu_key}")
            # Add the new key
            self.cache_data[key] = item
            self.frequency[key] = 1
            self.cache_order.append(key)

    def get(self, key):
        """
        Get an item by its key. Update its frequency.
        Args:
            key: The key of the item to get.
        Returns:
            The item if it is in the cache, None otherwise.
        """
        if key in self.cache_data:
            self.frequency[key] += 1
            # Maintain the order of keys based on frequency
            self.cache_order.remove(key)
            self.cache_order.append(key)
            return self.cache_data[key]
        return None
