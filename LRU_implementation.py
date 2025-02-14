from collections import OrderedDict
class LRUCache(OrderedDict):
    def __init__(self,capacity):
        self.capacity = capacity 
        self.cache = OrderedDict()
    def get(self,key:int) -> int: #O(1)
        if key in self.cache: 
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return -1
    def put(self,key:int,value:int): #O(1)
         if len(self.cache) >= self.capacity:
              self.cache.popitem(last=False)
         self.cache[key] = value
         self.cache.move_to_end(key)



cache = LRUCache(3)
cache.put(3,2)
cache.put(5,3)
cache.put(9,4)
print(cache.cache)
print(cache.get(5))
cache.put(8,3)
print(cache.cache)