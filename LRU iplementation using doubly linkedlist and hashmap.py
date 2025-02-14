class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        
        # Dummy head and tail nodes for easier manipulation of the list
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_node(self, node: Node):
        """Adds the new node right after the head (most recent)."""
        node.prev = self.head
        node.next = self.head.next
        
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node: Node):
        """Removes an existing node from the list."""
        if node is None:
            return
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None

    def move_to_head(self, node: Node):
        """Move an existing node to the front (head), making it the most recent."""
        self.remove_node(node)
        self.add_node(node)

    def pop_tail(self) -> Node:
        """Remove the last node before the dummy tail, which is the least recently used."""
        if self.tail.prev is self.head:  # If the list is empty
            return None
        tail_node = self.tail.prev
        self.remove_node(tail_node)
        return tail_node

    def get(self, key: int) -> int:
        """Retrieve the value from the cache, if present, and move the node to the front."""
        node = self.cache.get(key, None)
        if node is None:
            return -1  # Key not found
        self.move_to_head(node)
        return node.value

    def put(self, key: int, value: int):
        """Insert or update a key-value pair in the cache."""
        node = self.cache.get(key, None)
        if node is None:
            # If the node is not found, create a new one
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.add_node(new_node)
            
            # If the cache exceeds the capacity, evict the least recently used item
            if len(self.cache) > self.capacity:
                lru_node = self.pop_tail()
                if lru_node is not None:
                    del self.cache[lru_node.key]  # Remove the least recently used node from cache
        else:
            # If the node is found, update its value and move it to the front
            node.value = value
            self.move_to_head(node)
# Example Usage
lru_cache = LRUCache(3)
lru_cache.put(1, 1)
lru_cache.put(2, 2)
lru_cache.put(3, 3)
print(lru_cache.get(1))   # Output: 1, moves key 1 to the head
lru_cache.put(4, 4)       # Evicts key 2 (least recently used)
print(lru_cache.get(2))   # Output: -1, key 2 has been evicted
lru_cache.put(5, 5)       # Evicts key 3 (least recently used)
print(lru_cache.get(3))   # Output: -1, key 3 has been evicted
print(lru_cache.get(1))   # Output: 1, key 1 is still in the cache
print(lru_cache.get(4))   # Output: 4, key 4 is still in the cache
print(lru_cache.get(5))   # Output: 5, key 5 is still in the cache
