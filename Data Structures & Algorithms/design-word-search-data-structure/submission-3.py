class TrieNode:
    def __init__(self):
        self.children = {}
        self.EOW = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.EOW = True

    def search(self, word: str) -> bool:
        queue = deque()
        queue.append(self.root)
        for c in word:
            if c == '.':
                for i in range(len(queue)):
                    curr = queue.popleft()
                    for child in curr.children.values():
                        queue.append(child)
            else:
                new_queue = deque()
                for i in range(len(queue)):
                    curr = queue.popleft()
                    for child in curr.children:
                        if child == c:
                            new_queue.append(curr.children[child])
                if len(new_queue) == 0:
                    return False
                queue = new_queue
        for q in queue:
            if q.EOW:
                return True
        return False

                






