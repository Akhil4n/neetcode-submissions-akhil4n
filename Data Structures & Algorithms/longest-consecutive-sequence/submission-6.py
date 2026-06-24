class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        res = 0

        for n in seen:
            if n - 1 in seen:
                continue
            start = n
            while start + 1 in seen:
                start += 1
            res = max(res, start - n + 1)
        return res
            