class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, curr = [], []
        def backtrack(i, curSum, curr):
            if i >= len(nums):
                return
            if curSum == target:
                res.append(curr.copy())
                return
            elif curSum >= target:
                return
            curr.append(nums[i])
            backtrack(i, curSum + nums[i], curr)
            curr.pop()
            backtrack(i + 1, curSum, curr)
        backtrack(0, 0, [])
        return res