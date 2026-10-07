class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums)):
            curr = nums[i]

            for j in range(0, i):
                if nums[j] < curr:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)