from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for i in range(len(temperatures))]
        tStack = []
        for i, t in enumerate(temperatures):
            while tStack and t > tStack[-1][0]:
                tT, tI = tStack.pop()
                res[tI] = i - tI
            tStack.append([t, i])
        return res

