class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def backtrack(i, j, idx):
            if idx >= len(word):
                return True
            if min(i, j) < 0 or i >= rows or j >= cols or board[i][j] != word[idx]:
                return False
            
            temp = board[i][j]
            board[i][j] = "*"
            res = backtrack(i + 1, j, idx + 1) or backtrack(i - 1, j, idx + 1) or backtrack(i, j + 1, idx + 1) or backtrack(i, j - 1, idx + 1)
            board[i][j] = temp
            return res
            
        for r in range(rows):
            for j in range(cols):
                if board[r][j] == word[0]:
                    if backtrack(r, j, 0):
                        return True

        return False