class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2
        dp = [True] + [False] * target

        for x in nums:
            for i in range(target, x - 1, -1):
                if dp[i - x]:
                    dp[i] = True

        return dp[target]
        