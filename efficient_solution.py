from collections import OrderedDict

class NaiveLRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity
        
    def put(self, key: str, value: str):
        if key in self.cache:
            # Update the existing key's value and move it to the end to mark it as recently used
            self.cache.move_to_end(key)
        self.cache[key] = value
        
        if len(self.cache) > self.capacity:
            # Pop the first (least recently used) item from the cache
            self.cache.popitem(last=False)
        
    def get_value(self, key: str) -> str:
        if key in self.cache:
            # Move the accessed key to the end to mark it as recently used
            self.cache.move_to_end(key)
            return self.cache[key]
        return "-1"