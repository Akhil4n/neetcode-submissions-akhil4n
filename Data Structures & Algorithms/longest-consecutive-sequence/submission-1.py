class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        snums = set(nums)
        hmap = {}
        for x in snums:
            if x - 1 not in snums:
                hmap[x] = 1
        for x in hmap.keys():
            y = x + 1
            while y in snums:
                hmap[x] += 1
                y += 1
        if len(hmap) > 0:
            return max(hmap.values())
        return 0

