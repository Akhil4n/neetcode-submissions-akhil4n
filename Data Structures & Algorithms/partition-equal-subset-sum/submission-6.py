class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        cache = {}


        def dfs(i, curSum):
            if i >= len(nums):
                return curSum == 0
            if (i, curSum) in cache:
                return cache[(i, curSum)]
            num = nums[i]
            res = dfs(i + 1, curSum + num) or dfs(i + 1, curSum - num)
            cache[(i, curSum)] = res
            return res
        return dfs(0, 0)