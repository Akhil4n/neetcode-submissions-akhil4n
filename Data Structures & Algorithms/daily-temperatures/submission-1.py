class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for _ in range(len(temperatures))]
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                curr = stack.pop()
                res[curr[1]] = i - curr[1]
            stack.append([t, i])
        return res
