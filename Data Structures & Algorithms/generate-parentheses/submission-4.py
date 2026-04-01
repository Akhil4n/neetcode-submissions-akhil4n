class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(curr, numOpen, numClosed):
            if len(curr) == n * 2:
                res.append("".join(curr))
                return
            
            if numOpen < n:
                curr.append('(')
                backtrack(curr, numOpen + 1, numClosed)
                curr.pop()

            if numClosed < numOpen:
                curr.append(')')
                backtrack(curr, numOpen, numClosed + 1)
                curr.pop()

        backtrack([], 0, 0)
        return res