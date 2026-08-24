class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # [1, 1, -1, -1, 1, 1] -> 4
        res = float('-inf')
        for i in range(len(nums)):
            cursum = 0
            for j in range(i, len(nums) + i):
                val = nums[j % len(nums)]
                cursum += val
                res = max(res, cursum)
                if cursum < 0:
                    cursum = 0

        return res
