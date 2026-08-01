class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            curr = nums[m]
            if curr == target:
                return m
            elif curr > target:
                r = m - 1
            else:
                l = m + 1
        return -1
        