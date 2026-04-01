class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        res = 0

        for n in nums:
            if n - 1 not in seen:
                curr = n
                curRes = 1
                while curr + 1 in seen:
                        curRes += 1
                        curr += 1
                res = max(res, curRes)

        return res