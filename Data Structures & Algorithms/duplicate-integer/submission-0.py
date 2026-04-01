class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        y = []
        z = 2
        for i in range(len(nums)):
            if nums[i] not in y:
                y.append(nums[i])
            elif nums[i] in y:
                return True
                break
        return False

        
         