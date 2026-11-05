class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            lval, rval = nums[l], nums[r]
            val = nums[m]
            if val == target:
                return True
            if lval < val:
                if lval <= target < val:
                    r = m - 1
                else:
                    l = m + 1
            elif lval > val:
                if val < target <= rval:
                    l = m + 1
                else:
                    r = m - 1
            else:
                l += 1

        return False