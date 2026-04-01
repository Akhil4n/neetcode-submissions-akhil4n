class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def findHours(m, piles):
            res = 0
            for p in piles:
                res += math.ceil(p / m)
            return res
        l = 1
        r = max(piles)
        lastRes = 0
        while l <= r:
            m = (l + r) // 2
            key = findHours(m, piles)
            if key > h:
                l = m + 1
            else:
                lastRes = m
                r = m - 1
        return lastRes
        
