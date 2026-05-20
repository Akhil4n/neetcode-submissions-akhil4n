class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2:
            return False

        target = total // 2

        cache = {}

        def dfs(i, curSum):
            if curSum == 0:
                return True

            if curSum <= 0 or i == len(nums):
                return False

            if (i, curSum) in cache:
                return cache[(i, curSum)]

            res = False
            if dfs(i+1, curSum - nums[i]):
                res = True

            if dfs(i + 1, curSum):
                res = True

            cache[(i, curSum)] = res
            return res

        return dfs(0, target)