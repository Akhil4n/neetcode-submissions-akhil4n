class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []

        for i, h in enumerate(heights):
            add = (h, i)
            if not stack:
                stack.append(add)
                res = max(res, h)
            else:
                idx = i
                while stack and h < stack[-1][0]:
                    curr = stack.pop()
                    res = max(res, curr[0] * (i - curr[1]))
                    idx = curr[1]
                stack.append((h, idx))

        for pair in stack:
            res = max((len(heights) - pair[1]) * pair[0], res)
        
        return res