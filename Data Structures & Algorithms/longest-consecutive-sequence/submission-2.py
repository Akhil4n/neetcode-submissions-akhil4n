class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lcs = 0
        for n in nums:
            cs = 1
            while n+1 in nums:
                cs += 1
                n += 1
            lcs = max(lcs, cs)
        return lcs
                