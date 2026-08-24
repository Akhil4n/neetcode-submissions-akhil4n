class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # [1, 1, -1, -1, 1, 1] -> 4
        minsum, maxsum = float('inf'), float('-inf')
        currmin, currmax = 0, 0
        for num in nums:
            currmax += num
            maxsum = max(maxsum, currmax)
            if currmax < 0:
                currmax = 0
            
            currmin += num
            minsum = min(minsum, currmin)
            if currmin > 0:
                currmin = 0

        if maxsum < 0:
            return maxsum
        return max(maxsum, sum(nums) - minsum)
