class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, curr, curSum):
            if curSum == target:
                res.append(curr.copy())
                return
            if curSum > target or i >= len(nums):
                return
            curr.append(nums[i])
            backtrack(i, curr, curSum + nums[i])
            curr.pop()
            backtrack(i + 1, curr, curSum)
        
        backtrack(0, [], 0)
        return res