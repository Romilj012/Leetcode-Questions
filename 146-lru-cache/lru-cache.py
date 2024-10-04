class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.Keypairs = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.Keypairs:
            self.Keypairs.move_to_end(key)
            return self.Keypairs[key] 
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.Keypairs:
                self.Keypairs.move_to_end(key)
                self.Keypairs[key] = value
        else:
            if len(self.Keypairs) >= self.capacity:
                # first_key = list(self.Keypairs.keys())[0]
                self.Keypairs.popitem(last = False)
            self.Keypairs[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)