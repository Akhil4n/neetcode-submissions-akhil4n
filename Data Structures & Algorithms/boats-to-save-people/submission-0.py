class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        res = 0
        people.sort()
        # 1, 2, 2, 3, 3
        # 1, 2, 4, 5
        l, r = 0, len(people) - 1
        while l < r:
            lval, rval = people[l], people[r]
            if lval + rval <= limit:
                l += 1
            res += 1
            r -= 1

        if l == r:
            res += 1
        return res