class Solution:
    def rob(self, nums: List[int]) -> int:
        
        rob2, rob1 = 0, 0

        for n in nums:
            if n + rob2 > rob1:
                res = n + rob2
            else:
                res = rob1
            rob2 = rob1
            rob1 = res

        return rob1