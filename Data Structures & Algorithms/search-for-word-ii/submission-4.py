class TrieNode:
    def __init__(self):
        self.children = {}
        self.EOW = False

    def add_word(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.EOW = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        trie = TrieNode()
        for word in words:
            trie.add_word(word)
        
        res = []

        rows = len(board)
        cols = len(board[0])
        def backtrack(r, c, node, word):
            if min(r, c) < 0 or r >= rows or c >= cols or board[r][c] not in node.children:
                return
            
            temp = board[r][c]
            word.append(temp)
            node = node.children[board[r][c]]
            if node.EOW:
                res.append(''.join(word))
                node.EOW = False
                
            board[r][c] = "#"
            backtrack(r + 1, c, node, word)
            backtrack(r - 1, c, node, word)
            backtrack(r, c + 1, node, word)
            backtrack(r, c - 1, node, word)
            word.pop()
            board[r][c] = temp

        for r in range(rows):
            for c in range(cols):
                backtrack(r, c, trie, [])
        
        return res

    