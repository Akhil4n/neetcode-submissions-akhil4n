class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}

        def dp(i, side):
            if i >= len(prices):
                return 0
            if (i, side) in cache:
                return cache[(i, side)]
            if side == 'b':
                res = max(dp(i + 1, 'b'), dp(i + 1, 's') - prices[i])
            else:
                res = max(dp(i + 2, 'b') + prices[i], dp(i + 1, 's'))
            cache[(i, side)] = res
            return res

        return dp(0, 'b')