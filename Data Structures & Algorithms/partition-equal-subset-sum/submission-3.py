class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2:
            return False

        target = total // 2

        def dfs(i, curSum):
            if curSum == target:
                return True

            if curSum > target or i == len(nums):
                return False

            if dfs(i+1, curSum + nums[i]):
                return True

            return dfs(i + 1, curSum)

        return dfs(0, 0)