class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums) - 1
        mVal = float('inf')
        while l < r:
            if r - l == 1:
                return min(nums[l], nums[r])
            m = (l + r) // 2
            key = nums[m]
            if key > nums[l]:
                l = m
            else:
                mVal = min(mVal, nums[m])
                r = m
        return mVal
