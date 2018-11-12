# August 3, 2018

"""
This problem was asked by Google.

Implement an LFU (Least Frequently Used) cache. It should be able
to be initialized with a cache size n, and contain the following
methods:

set(key, value): sets key to value. If there are already n items
    in the cache and we are adding a new item, then it should
    also remove the least frequently used item. If there is a tie,
    then the least recently used key should be removed.

get(key): gets the value at key. If no such key exists, return null.

Each operation should run in O(1) time.
"""
from collections import defaultdict
from time import time

class Cache:
    def __init__(self, max_items):
        self.max_items = max_items	                    # max concurrent cache items
        self.cache = dict()                             # cache is stored -> (key, val)
        self.hits = defaultdict(int)                    # cache access count
        self.timestamps = defaultdict(lambda: time())   # cache access timestamp

    @property
    def cache_full(self):
        return len(self.cache) == self.max_items

    def set(self, key, val):
        if self.cache_full: # remove least used item to free up space
            # 
            lru_num_hits = min(self.hits.values()) if self.hits else 0

            # get all the items that have the same lowest num of hits
            lru_items = [k for k, v in self.hits.items() if self.hits[k] == lru_num_hits]

            # filter the items for the most recently used item based on timestamp
            lru_item = min(lru_items, key=lambda k: self.timestamps[k])
            self.cache.pop(lru_item)
            self.hits.pop(lru_item)
            self.timestamps.pop(lru_item)

        self.cache[key] = val
        self.hits.setdefault(key, 0)
        self.timestamps.setdefault(key, time())

    def get(self, key):
        print(self.cache)
        if key not in self.cache:
            return None

        self.hits[key] += 1
        self.timestamps[key] = time()
        return self.cache[key]

    def __str__(self):
        ret = "--- Cache entries:\n"
        for i, (k, v) in enumerate(self.cache.items()):
            ret += f"{i+1} -> key: {k}, val: {v}, hits: {self.hits[k]}, ts: {self.timestamps[k]}\n"
        return ret


if __name__ == '__main__':
    # TODO -> test cache implementation
    cache = Cache(max_items=5)

    assert cache.get("nothing here") is None

    pokemon = [
        ("bulbasaur", "venusaur"),
        ("psyduck", "abra"),
        ("charmeleon", "charmander"),
        ("squirtle", "wartortle"),
        ("pikachu", "raichu"),
        # inserting item below should remove
        ("eevee", "jolteon"),
        ("seel", "haunter")
    ]
    for start, final in pokemon:
        cache.set(start, final)

    print(cache.get("charmeleon")) is "charmander"

