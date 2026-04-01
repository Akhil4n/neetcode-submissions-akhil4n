class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.nxt = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.mapping = {}

        self.left = Node()   # LRU sentinel
        self.right = Node()  # MRU sentinel

        self.left.nxt = self.right
        self.right.prev = self.left

    def remove(self, node):
        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev

    def insert(self, node):
        prev = self.right.prev
        prev.nxt = node
        node.prev = prev
        node.nxt = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.mapping:
            return -1

        node = self.mapping[key]

        # move to MRU
        self.remove(node)
        self.insert(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.mapping:
            self.remove(self.mapping[key])

        node = Node(key, value)
        self.mapping[key] = node
        self.insert(node)

        if len(self.mapping) > self.cap:
            # evict LRU
            lru = self.left.nxt
            self.remove(lru)
            del self.mapping[lru.key]