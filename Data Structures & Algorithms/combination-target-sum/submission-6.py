class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        def backtrack(i, cursum):
            if cursum == target:
                res.append(curr.copy())
                return
            if i >= len(nums) or cursum >= target:
                return
            
            curr.append(nums[i])
            backtrack(i, cursum + nums[i])
            curr.pop()
            backtrack(i + 1, cursum)
            
        backtrack(0, 0)
        return res