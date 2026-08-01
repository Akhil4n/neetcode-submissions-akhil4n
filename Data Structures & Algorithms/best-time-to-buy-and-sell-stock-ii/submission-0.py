class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bp = None
        res = 0
        for p in prices:
            if bp is None:
                bp = p
                continue

            if p > bp:
                res += p - bp
            bp = p

        return res
