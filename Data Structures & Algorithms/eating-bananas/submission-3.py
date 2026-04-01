class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def calculateHours(r):
            res = 0
            for p in piles:
                res += math.ceil(p / r)
            return res

        l, r = 1, max(piles)

        while l <= r:
            m = (l + r) // 2
            check = calculateHours(m)
            if check > h:
                l = m + 1
            elif check <= h:
                r = m - 1

        return l

