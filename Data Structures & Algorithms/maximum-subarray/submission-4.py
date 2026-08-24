class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        curr = 0
        for num in nums:
            if curr + num > 0:
                curr += num
                res = max(res, curr)
            else:
                res = max(res, num)
                curr = 0
        return res