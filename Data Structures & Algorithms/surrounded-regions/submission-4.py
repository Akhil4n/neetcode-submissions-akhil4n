class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(i, j):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] == "X" or board[i][j] == "B":
                return
            board[i][j] = "B"
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        for i in range(len(board)):
            if i == 0 or i == len(board) - 1:
                for j in range(len(board[i])):
                    if board[i][j] == "O":
                        dfs(i, j)
            else:
                if board[i][0] == "O":
                    dfs(i, 0)
                if board[i][len(board[i]) - 1] == "O":
                    dfs(i, len(board[i]) - 1)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "B":
                    board[i][j] = "O"       
            