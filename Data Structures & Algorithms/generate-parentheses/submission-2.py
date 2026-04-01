class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        #backtracking function
        def backtrack(curr, numOpen, numClosed):
            if len(curr) == n * 2 and numOpen == numClosed:
                res.append(curr)
                return
            if len(curr) == n * 2 and numOpen != numClosed:
                return
            if numOpen < numClosed:
                return
            curr += "("
            backtrack(curr, numOpen + 1, numClosed)
            curr = curr[0:len(curr) - 1]
            if numOpen > numClosed:
                curr += ")"
                backtrack(curr, numOpen, numClosed + 1)
        
        backtrack("", 0, 0)
        return res
