class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            curVal = nums[i]
            if i + curVal >= target:
                target = i
        return target == 0