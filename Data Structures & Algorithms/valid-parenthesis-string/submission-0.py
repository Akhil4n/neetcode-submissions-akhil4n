class Solution:
    def checkValidString(self, s: str) -> bool:
        astInds = deque()
        rstack = []
        lstack = []

        for i in range(len(s)):
            curr = s[i]
            if curr == "*":
                astInds.append(i)
            elif curr == "(":
                rstack.append(i)
            else:
                if len(rstack) > 0:
                    rstack.pop()
                else:
                    lstack.append(i)
        end = len(rstack) - 1
        for i in range(end, -1, -1):
            if astInds and astInds[-1] > rstack[i]:
                astInds.pop()
                rstack.pop()

        end = len(lstack)
        removed = 0
        for i in range(end):
            if astInds and astInds[0] < lstack[i]:
                astInds.popleft()
                removed += 1
        
        return removed == len(lstack) and len(rstack) == 0