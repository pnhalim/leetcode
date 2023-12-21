class Node:
    
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.lru_head = None # this is the most recent
        self.lru_tail = None # this is the least recent
        self.data = {} # stores a node
        
    def print_lru(self):
        s = []
        n = self.lru_head
        while n:
            s.append(str(n.value))
            n = n.next
        print(f"LRU Cache: {' '.join(s)}")
        
        s = []
        n = self.lru_tail
        while n:
            s.append(str(n.value))
            n = n.prev
        print(f"LRU Cache: {' '.join(s[::-1])}")
        
        print(self.data)
        
    def update_lru(self, key: int) -> None:
        node = self.data[key]
        if node == self.lru_head:
            return
        if node == self.lru_tail:
            self.lru_tail = node.prev
        
        if node.next:
            node.next.prev = node.prev
        if node.prev:
            node.prev.next = node.next
        
        if self.lru_head:
            self.lru_head.prev = node
            node.next = self.lru_head
            node.prev = None
            self.lru_head = node
        else:
            self.lru_head = self.lru_tail = node
        
    def get(self, key: int) -> int:    
        # print("GET")
        if key in self.data:
            self.update_lru(key)
            # self.print_lru()
            return self.data[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            self.update_lru(key)
            self.data[key].value = value
        else:
            node = Node(key, value)
            self.data[key] = node
            if self.lru_head:
                self.lru_head.prev = node
                node.next = self.lru_head
                self.lru_head = node
            else:
                self.lru_head = self.lru_tail = node
            self.size += 1
            
            if self.size > self.capacity:
                key_to_delete = self.lru_tail.key
                if self.lru_tail.prev:
                    self.lru_tail.prev.next = None
                self.lru_tail = self.lru_tail.prev
                del self.data[key_to_delete]
        
#         print("PUT")
#         self.print_lru()
            
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)