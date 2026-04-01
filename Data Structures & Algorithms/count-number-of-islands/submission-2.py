class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "0":
                return 100
            grid[i][j] = "0"
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
            return 1
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                val = grid[i][j]
                if val == "1":
                    res += dfs(i, j)
        return res