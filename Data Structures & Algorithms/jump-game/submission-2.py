class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[0] = True
        for i in range(len(nums)):
            curr = nums[i]
            if dp[i] == True:
                for v in range(curr):
                    if i + 1 + v < len(dp):
                        dp[i + 1 + v] = True
        print(dp)
        return dp[-1]