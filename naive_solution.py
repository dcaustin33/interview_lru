class NaiveLRUCache:
    def __init__(self, capacity: int):
        self.cache = []
        self.keys = set()
        self.capacity = capacity
        
    def remove(self, key: str):
        for i, (k, v) in enumerate(self.cache):
            if k == key:
                self.cache.pop(i)
                break
        self.keys.remove(key)
        
    def _get(self, key: str) -> str:
        """returns the index of the key in the cache"""
        for i, (k, v) in enumerate(self.cache):
            if k == key:
                return i
        

    def put(self, key: str, value: str):
        # first we need to check if the key is already in the cache
        if key in self.keys:
            # if it is, we need to remove it from the cache
            self.remove(key)
        
        # next we need to check if the cache is full
        if len(self.cache) == self.capacity:
            # if it is we remove the first element
            key, value = self.cache.pop(0)
            self.keys.remove(key)
            
        # finally we add the new key value pair to the cache
        self.cache.append((key, value))
        self.keys.add(key)

    def get_value(self, key: str) -> str:
        """Gets the value of the key if the key exists in the cache"""
        if key in self.keys:
            idx = self._get(key)
            key, value = self.cache.pop(idx)
            self.cache.append((key, value))
            return value
        return "-1"