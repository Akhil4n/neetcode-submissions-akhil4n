class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float("-inf")
        curSum = 0
        for n in nums:
            res = max(res, curSum + n)
            if curSum + n < 0:
                curSum = 0
            else:
                curSum += n
        return res