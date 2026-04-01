class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            curr = nums[i]
            if i + curr >= goal:
                goal = i
        return goal == 0