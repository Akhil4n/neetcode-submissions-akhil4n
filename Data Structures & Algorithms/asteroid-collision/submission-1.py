class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        right_stack = []
        left = []
        for asteroid in asteroids:
            if asteroid > 0:
                right_stack.append(asteroid)
            else:
                gone = False
                while right_stack and right_stack[-1] <= abs(asteroid):
                    val = right_stack.pop()
                    if val == abs(asteroid):
                        gone = True
                        break
                if not right_stack and not gone:
                    left.append(asteroid)
        res = []
        for asteroid in left:
            res.append(asteroid)
        for asteroid in right_stack:
            res.append(asteroid)
        return res