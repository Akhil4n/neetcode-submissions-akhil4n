class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        """
        Do not return anything, modify nums in-place instead.
        """
        res = []
        for i in range(len(nums) - k, len(nums) - k + len(nums)):
            idx = i % len(nums)
            res.append(nums[idx])
        print(res)
        for i in range(len(res)):
            nums[i] = res[i]







        