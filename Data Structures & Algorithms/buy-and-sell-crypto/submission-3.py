class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        bp = float("inf")

        for i in range(len(prices)):
            mp = max(mp, prices[i] - bp)
            bp = min(bp, prices[i])

        return mp