class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.res = False
        self.board = board
        self.word = word
        seen = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    self.backtrack(i, j, 0, seen)
        return self.res
    def backtrack(self, row, col, i, seen):
            if i == len(self.word):
                self.res = True
                return
            if row < 0 or row >= len(self.board) or col < 0 or col >= len(self.board[0]) or self.board[row][col] != self.word[i] or (row, col) in seen:
                return
            seen.add((row, col))
            self.backtrack(row + 1, col, i + 1, seen)
            self.backtrack(row - 1, col, i + 1, seen)
            self.backtrack(row, col + 1, i + 1, seen)
            self.backtrack(row, col - 1, i + 1, seen)
            seen.remove((row, col))