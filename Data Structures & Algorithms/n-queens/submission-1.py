class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set()
        negDiag = set()

        res = []
        board = [["."] * n for _ in range(n)]
        rows = cols = n

        def backtrack(r, c):
            if r >= rows:
                add = ["".join(board_row) for board_row in board]
                res.append(add)
                return
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                return
            board[r][c] = "Q"
            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            if r == rows - 1:
                backtrack(r + 1, c)
            else:
                for i in range(cols):
                    backtrack(r + 1, i)
            board[r][c] = "."
            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
        
        for i in range(n):
            backtrack(0, i)
        return res

            