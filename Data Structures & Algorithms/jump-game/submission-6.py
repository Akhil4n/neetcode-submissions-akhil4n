class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            curr = nums[i]
            if i + curr >= target:
                target = i
        return target == 0