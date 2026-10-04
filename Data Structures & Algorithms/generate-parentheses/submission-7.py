class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, curr = [], []

        def backtrack(opn, cls):
            if opn > n or cls > opn:
                return
            if opn == cls and opn == n:
                res.append("".join(curr))
                return
            
            curr.append('(')
            backtrack(opn + 1, cls)
            curr.pop()
            curr.append(')')
            backtrack(opn, cls + 1)
            curr.pop()

        backtrack(0, 0)
        return res