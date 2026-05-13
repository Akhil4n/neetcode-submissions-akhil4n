class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = rob2 = 0

        for n in nums:
            temp = rob2
            if rob1 + n > rob2:
                rob2 = rob1 + n
            rob1 = temp
        
        return rob2