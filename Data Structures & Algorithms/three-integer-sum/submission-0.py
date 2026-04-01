class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            val = nums[i]
            target = 0 - val
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = val + nums[l] + nums[r]
                if  total == 0 and [val, nums[l], nums[r]] not in res:
                    res.append([val, nums[l], nums[r]])
                elif total > 0:
                    r -= 1
                else:
                    l += 1
        return res