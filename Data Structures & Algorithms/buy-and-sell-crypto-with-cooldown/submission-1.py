class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        
        def dfs(i: int, cond: bool):
            if i >= len(prices):
                return 0
            if (i, cond) in dp:
                return dp[(i, cond)]
            if cond:
                res = max(dfs(i + 1, False) - prices[i], dfs(i + 1, True))
            else:
                res = max(dfs(i + 2, True) + prices[i], dfs(i + 1, False))
            dp[(i, cond)] = res
            return res
        return dfs(0, True)

                
