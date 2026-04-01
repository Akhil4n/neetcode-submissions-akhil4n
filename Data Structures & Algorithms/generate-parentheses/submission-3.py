class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtrack(numOpen, numClosed):
            if len(stack) == 2 * n:
                res.append("".join(stack))
                return

            if numOpen < n:
                stack.append("(")
                backtrack(numOpen + 1, numClosed)
                stack.pop()

            if numClosed < numOpen:
                stack.append(")")
                backtrack(numOpen, numClosed + 1)
                stack.pop()

        backtrack(0, 0)
        return res