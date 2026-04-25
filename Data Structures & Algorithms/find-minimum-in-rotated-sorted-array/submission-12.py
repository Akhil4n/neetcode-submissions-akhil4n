class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            lVal, mVal, rVal = nums[l], nums[m], nums[r]

            if lVal > rVal:
                if mVal < lVal:
                    r = m
                    l += 1
                else:
                    l = m + 1
            else:
                return nums[l]

        return nums[l]