class Solution:
    def rob(self, nums: List[int]) -> int:
        robf = robc = 0
        for n in nums:
            temp = 0
            if robf + n > robc:
                temp = robf + n
            else:
                temp = robc
            robf = robc
            robc = temp
        return robc
