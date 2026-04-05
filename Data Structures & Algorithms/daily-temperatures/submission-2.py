class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            curr = temperatures[i]
            while stack and stack[-1][0] < curr:
                temp, ind = stack.pop()
                res[ind] = i - ind
            stack.append((curr, i))
        return res