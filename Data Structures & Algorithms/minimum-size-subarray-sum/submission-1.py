class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        l = 0
        cur_sum = 0
        for r in range(len(nums)):
            cur_sum += nums[r]
            if cur_sum >= target:
                res = min(res, r - l + 1)
            while l < r and cur_sum >= target:
                cur_sum -= nums[l]
                l += 1
                if cur_sum < target:
                    break
                res = min(res, r - l + 1)
        return res if res != float('inf') else 0