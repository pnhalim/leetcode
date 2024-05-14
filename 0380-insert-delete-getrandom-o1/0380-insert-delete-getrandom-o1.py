class RandomizedSet:

    def __init__(self):
        self.hash = {}

    def insert(self, val: int) -> bool:
        if val in self.hash:
            return False
        self.hash[val] = 0
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hash:
            return False
        del self.hash[val]
        return True
    
    def getRandom(self) -> int:
        return random.choice(list(self.hash.keys()))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()