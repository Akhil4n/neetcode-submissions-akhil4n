class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMin = None
        curMax = None
        res = float('-inf')
        for n in nums:
            if not curMin and not curMax:
                curMin = curMax = n
            elif n >= 0:
                curMax = max(n, curMax * n)
                curMin = min(n, curMin * n)
            else:
                temp = curMax
                curMax = max(n, curMin * n)
                curMin = min(n, temp * n)
            res = max(curMax, res)
        return res