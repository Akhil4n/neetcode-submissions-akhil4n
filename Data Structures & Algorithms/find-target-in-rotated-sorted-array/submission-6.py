class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                r = i
        print(r)
        if nums[0] > target:
            l = r + 1
            r = len(nums) - 1
        print(l, r)
        while l < r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        if l < len(nums) and nums[l] == target:
            return l
        return -1
        