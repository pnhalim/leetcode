class Node:

    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.data = {}          # <key, node(key, val)>
        self.lru_head = None    # the most recently used
        self.lru_tail = None    # the least recently used
        
    def print_lru(self) -> None:
        print("printing lru...")
        print(self.data)
        # forward
        s = []
        n = self.lru_head
        while n:
            s.append(str(n.val))
            n = n.next
        print(f"lru: {' '.join(s)}")
        # backward
        s = []
        n = self.lru_tail
        while n:
            s.append(str(n.val))
            n = n.prev
        print(f"lru: {' '.join(s[::-1])}")

    def update_lru(self, key: int) -> None:
        """Updates the lru linked-list to put the key at the beginning."""
        node = self.data[key]
        # remove node from list
        if node == self.lru_head:
            return
        elif node == self.lru_tail:
            self.lru_tail = self.lru_tail.prev
            self.lru_tail.next = None
        else:
            prev = node.prev
            next = node.next
            if prev:
                prev.next = node.next
            if next:
                next.prev = node.prev
        node.prev = None
        node.next = None
        # add to beginning of lru
        if not self.lru_head:
            self.lru_head = node
            self.lru_tail = node
        else:
            self.lru_head.prev = node
            node.next = self.lru_head
            self.lru_head = node
        # self.print_lru()


    def get(self, key: int) -> int:
        """Returns the val of key if exists. Else, returns -1."""
        if key in self.data:
            self.update_lru(key)
            return self.data[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        """Updates or adds element to lru."""
        if key in self.data:
            self.update_lru(key)
            self.data[key].val = value
        else:
            self.add(key, value)
            # self.print_lru()

    def add(self, key: int, value: int) -> None:
        """Adds the node to the beginning of the lru."""
        # add to dictionary
        node = Node(key, value)
        self.data[key] = node
        self.size += 1        
        # add node
        if not self.lru_head:
            self.lru_head = node
            self.lru_tail = node
        else:
            self.lru_head.prev = node
            node.next = self.lru_head
            self.lru_head = node
        # check for evict
        if self.size > self.capacity:
            self.evict()

    def evict(self) -> None:
        """Evicts the last element in the lru, pointed to by self.lru_tail."""
        # remove from dictionary
        key = self.lru_tail.key
        del self.data[key]
        # remove node
        self.lru_tail = self.lru_tail.prev
        self.lru_tail.next = None
        self.size -= 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# lru = LRUCache(capacity=2)
# lru.put(1, 1)
# lru.put(2, 2)
# lru.get(1)
# lru.put(3, 3)
# lru.get(2)
# lru.put(4, 4)
# lru.get(1)
# lru.get(3)
# lru.get(4)