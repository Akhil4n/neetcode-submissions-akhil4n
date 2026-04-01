class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i in range(len(nums)):
            need = target - nums[i]
            if need in hmap:
                return [hmap[need], i]
            else:
                hmap[nums[i]] = i