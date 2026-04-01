class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def dfs(i, curr):
            if i >= len(nums):
                res.append(curr.copy())
                return
            curr.append(nums[i])
            dfs(i+1, curr)
            curr.pop()
            n = i + 1
            while n < len(nums) and nums[n] == nums[n-1]:
                n += 1
            dfs(n, curr)
        dfs(0, [])
        return res