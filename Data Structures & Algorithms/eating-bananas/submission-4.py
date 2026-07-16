class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        def can_eat(rate):
            hours = 0
            for p in piles:
                hours += math.ceil(p / rate)
                if hours > h:
                    return False
            return True
        
        while l < r:
            m = (l + r) // 2
            if can_eat(m):
                r = m
            else:
                l = m + 1
        return l
