class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        res = 0
        l, r = 0, len(height) - 1
        lMax, rMax = height[l], height[r]
        while l < r:
            if lMax <= rMax:
                l += 1
                add = lMax - height[l]
                if add > 0:
                    res += add
                lMax = max(lMax, height[l])
            else:
                r -= 1
                add = rMax - height[r]
                if add > 0:
                    res += add
                rMax = max(rMax, height[r])
        return res