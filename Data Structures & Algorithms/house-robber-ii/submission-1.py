class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        rob1, rob2 = 0, 0
        res1 = 0
        for i in range(len(nums) - 1):
            cur = nums[i]
            temp = max(cur + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        res1 = rob2
        rob1, rob2 = 0, 0
        res2 = 0
        for i in range(1, len(nums)):
            cur = nums[i]
            temp = max(cur + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        res2 = rob2
        return max(res1, res2)