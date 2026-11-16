class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(open, closed, curr):
            if open > n or closed > open:
                return
            if n == open == closed:
                res.append(curr.copy())
                return

            curr.append('(')
            backtrack(open + 1, closed, curr)
            curr.pop()

            curr.append(')')
            backtrack(open, closed + 1, curr)
            curr.pop()
            
        backtrack(0, 0, [])

        final = []
        for item in res:
            final.append("".join(item))
        return final