class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        wmap = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if val in wmap:
                return [wmap[val], i]
            else:
                wmap[nums[i]] = i
