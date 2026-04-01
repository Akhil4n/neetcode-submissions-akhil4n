class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            curr = nums[i]

            for j in range(i, len(nums)):
                if nums[j] > curr:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)    
