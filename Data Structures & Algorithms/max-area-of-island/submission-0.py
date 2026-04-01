class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        def dfs(i, j, grid):
            if i > len(grid) - 1 or i < 0 or j > len(grid[i]) - 1 or j < 0 or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            return 1 + dfs(i-1, j, grid) + dfs(i+1, j, grid) + dfs(i, j-1, grid) + dfs(i, j+1, grid)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(i, j , grid))
        return maxArea