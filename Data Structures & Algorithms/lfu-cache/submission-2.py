class ListNode:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None

class LinkedList:

    def __init__(self):
        self.left = ListNode(0, 0)
        self.right = ListNode(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
        self.size = 0

    def length(self):
        return self.size

    def pushRight(self, node):
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node
        self.size += 1

    def pop(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
        node.prev = None
        node.next = None
        self.size -= 1

    def popLeft(self):
        if self.length() == 0:
            return None
        node = self.left.next
        self.pop(node)
        return node

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.lfuCnt = 0
        self.kMap = {} # keys to node
        self.freqMap = defaultdict(LinkedList) # freqs to ll buckets
        
    def counter(self, node):
        cnt = node.freq
        node.freq += 1
        self.freqMap[cnt].pop(node)
        self.freqMap[cnt + 1].pushRight(node)
        if cnt == self.lfuCnt and self.freqMap[cnt].length() == 0:
            self.lfuCnt += 1


    def get(self, key: int) -> int:
        if key not in self.kMap:
            return -1

        node = self.kMap[key]
        self.counter(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.kMap:
            node = self.kMap[key]
            node.val = value
            self.counter(node)
            return
        
        if len(self.kMap) == self.cap:
            rem = self.freqMap[self.lfuCnt].popLeft()
            self.kMap.pop(rem.key)

        node = ListNode(key, value)
        self.kMap[key] = node
        self.freqMap[1].pushRight(node)
        self.lfuCnt = 1


