class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for i in range(len(position)):
            stack.append((position[i], speed[i]))
        res = 1
        stack.sort(reverse=True)
        time = (target - stack[0][0]) / stack[0][1]
        for i in range(1, len(stack)):
            currTime = (target - stack[i][0]) / stack[i][1]
            if currTime > time:
                res += 1
                time = currTime

        return res


