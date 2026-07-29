class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])

        dp = [1] * cols
        for i in range(cols):
            if obstacleGrid[0][i] == 0:
                dp[i] = dp[i - 1]
            else:
                dp[i] = 0
        print(dp)
        for r in range(1, rows):
            if obstacleGrid[r][0] == 1:
                dp[0] = 0
            for c in range(1, cols):
                if obstacleGrid[r][c] == 0:
                    dp[c] = dp[c] + dp[c - 1]
                else:
                    dp[c] = 0
            print(dp)

        return dp[-1]