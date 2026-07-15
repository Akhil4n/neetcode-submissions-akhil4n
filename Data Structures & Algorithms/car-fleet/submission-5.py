class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sps = []
        for i in range(len(position)):
            sps.append((position[i], speed[i]))
        sps.sort(reverse = True)

        stack = []
        for p, s in sps:
            stack.append((target - p) / s)
            while len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)


