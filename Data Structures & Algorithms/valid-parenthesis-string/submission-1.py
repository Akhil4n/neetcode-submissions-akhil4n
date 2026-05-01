class Solution:
    def checkValidString(self, s: str) -> bool:
        astInds = deque()
        stack = []

        for i in range(len(s)):
            curr = s[i]
            if curr == "*":
                astInds.append(i)
            elif curr == "(":
                stack.append(i)
            else:
                if len(stack) > 0:
                    stack.pop()
                elif len(astInds) > 0:
                    astInds.popleft()
                else:
                    return False

        for i in range(len(stack) - 1, -1, -1):
            if not astInds or astInds[-1] < stack[i]:
                return False
            astInds.pop()

        return True