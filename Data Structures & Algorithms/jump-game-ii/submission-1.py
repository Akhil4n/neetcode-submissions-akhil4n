class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        res = 0
        dp = [1001] * len(nums)
        dp[len(nums) - 1] = 0
        for i in range(len(nums) - 2, -1, -1):
            print(i)
            curr = nums[i]
            if curr == 0:
                continue
            jmp = min(i + curr, len(nums) - 1)
            minJ = min(dp[i + 1:jmp + 1])
            dp[i] = 1 + minJ
        return dp[0]


