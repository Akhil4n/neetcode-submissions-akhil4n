class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j, grid):
            if i > len(grid) - 1 or i < 0 or j > len(grid[0]) - 1 or j < 0 or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            dfs(i+1, j, grid)
            dfs(i-1, j, grid)
            dfs(i, j+1, grid)
            dfs(i, j-1, grid)
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    res += 1
                    dfs(i, j, grid)
        return res
