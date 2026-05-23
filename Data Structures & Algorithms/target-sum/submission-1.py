class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def dfs(i, curSum):
            if (i, curSum) in cache:
                return cache[(i, curSum)]
            if i == len(nums):
                if curSum == target:
                    return 1
                return 0
            res = dfs(i + 1, curSum + nums[i]) + dfs(i + 1, curSum - nums[i])
            cache[(i, curSum)] = res
            return res
        return dfs(0, 0)
