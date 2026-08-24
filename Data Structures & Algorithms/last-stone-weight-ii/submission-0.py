class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        total = sum(stones)
        target = (total + 1) // 2
        cache = {}
        def smash(i, pile):
            if i >= len(stones) or pile >= target:
                return abs(pile - (total - pile))
            if (i, pile) in cache:
                return cache[(i, pile)]

            res = min(smash(i + 1, pile), smash(i + 1, pile + stones[i]))
            cache[(i, pile)] = res
            return cache[(i, pile)]

        return smash(0, 0)