#!/usr/bin/env python3

'''Task 1: FIFO caching
'''


from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''A class `FIFOCache` that inherits from
       `BaseCaching` and is a caching system.
    '''

    def __init__(self):
        """ Initialize FIFOCache """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache using FIFO algorithm """
        if key is not None and item is not None:
            # Check if the cache is full
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the first item added to the cache (FIFO)
                first_key = next(iter(self.cache_data))
                # Discard the first item
                del self.cache_data[first_key]
                print("DISCARD:", first_key)

            # Add the new item to the cache
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key is not None:
            return self.cache_data.get(key)
