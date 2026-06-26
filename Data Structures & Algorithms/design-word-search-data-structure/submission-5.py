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
        

        def dfs(node, i):
            if i >= len(word):
                return node.EOW
            char = word[i]
            if char != '.':
                if char not in node.children:
                    return False
                else:
                    return dfs(node.children[char], i + 1)
            else:
                for child in node.children:
                    if dfs(node.children[child], i + 1):
                        return True
                return False
        
        return dfs(self.root, 0)


                






