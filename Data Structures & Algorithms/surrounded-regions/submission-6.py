class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def find_free(i, j):
            if min(i, j) < 0 or i >= rows or j >= cols or board[i][j] != 'O':
                return
            board[i][j] = '*'
            find_free(i + 1, j)
            find_free(i - 1, j)
            find_free(i, j + 1)
            find_free(i, j - 1)

        for c in range(cols):
            find_free(0, c)
            find_free(rows - 1, c)

        for r in range(rows):
            find_free(r, 0)
            find_free(r, cols - 1)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '*':
                    board[r][c] = 'O'