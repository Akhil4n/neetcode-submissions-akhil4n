class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            curr = abs(nums[i])
            ind = curr - 1
            if nums[ind] < 0:
                return curr
            else:
                nums[ind] *= -1
