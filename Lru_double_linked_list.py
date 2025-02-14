class Node:
    def __init__(self,key:int,value:int):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
class LRUcache:
    def __init__(self,capacity):
        self.capacity = capacity 
        self.cache = {}
        #dummy head and tail
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def add_node(self,node:Node):
        "add the new node in the right after head (most recent)"
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    def remove_node(self,node:Node):
        if node is None:
            return 
        node.next.prev = node.prev
        node.prev.next = node.next
        node.next = None
        node.prev = None 
    
    def move_to_head(self,node:Node):
        self.remove_node(node)
        self.add_node(node)
        
    def pop_tail(self)->Node:
        if self.tail.prev is self.head:
            return
        tail_node = self.tail.prev
        self.remove(tail_node)
        return tail_node

    def get(self,key:int)->int:
        node = self.cache.get(key,None)
        if node is None :
            return -1
        self.move_to_head(node)
        return node.value
    def put(self,key:int,value:int):
        node = self.cache.get(key,None)
        if node is None:
            new_node = Node(key,value)
            self.cache[key] = new_node
            self.add_node(new_node)
            if len(self.cache) > self.capacity:
                lru_node = self.pop_tail()
                if lru_node is not None:
                    del self.cache[lru_node.key]
        else:
            node.value = value
            self.move_to_head(node)





    

    

        
        
    
        
    