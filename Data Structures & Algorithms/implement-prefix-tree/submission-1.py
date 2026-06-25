class PrefixTree:

    def __init__(self):
        self.tree = {}

    def insert(self, word: str) -> None:
        key = ""
        for c in word:
            key += c
            if key not in self.tree:
                self.tree[key] = False
        self.tree[word] = True

    def search(self, word: str) -> bool:
        if word in self.tree and self.tree[word]:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        return prefix in self.tree
        