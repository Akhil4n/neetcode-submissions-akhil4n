class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = []
        for x in nums:
            if x in hashset:
                return True
            hashset.append(x)
        return False
        
         