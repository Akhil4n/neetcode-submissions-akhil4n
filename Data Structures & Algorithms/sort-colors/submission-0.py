class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = Counter(nums)
        idx = 0
        for i in range(counts[0]):
            nums[idx] = 0
            idx += 1
        for i in range(counts[1]):
            nums[idx] = 1
            idx += 1
        for i in range(counts[2]):
            nums[idx] = 2
            idx += 1
        