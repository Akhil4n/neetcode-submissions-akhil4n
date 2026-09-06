class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(1, -1, -1):
                if j == 1:
                    sell = prices[i] + dp[i + 2][0] if i + 2 < n else prices[i]
                    cooldown = dp[i + 1][1] if i + 1 < n else 0
                    dp[i][1] = max(sell, cooldown)
                else:
                    buy = dp[i + 1][1] - prices[i] if i + 1 < n else -prices[i]
                    cooldown = dp[i + 1][0] if i + 1 < n else 0
                    dp[i][0] = max(buy, cooldown)

        return dp[0][0]
