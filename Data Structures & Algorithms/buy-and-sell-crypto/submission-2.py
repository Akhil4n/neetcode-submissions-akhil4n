class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mP = 0
        for i in range(len(prices) - 1):
            mP = max(max(prices[i+1::]) - prices[i], mP)
        return mP
            


