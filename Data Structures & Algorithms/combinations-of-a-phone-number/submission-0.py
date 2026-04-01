class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        vals = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs","8":"tuv", "9":"wxyz"}
        if len(digits) == 0:
            return []
        def backtrack(i, curr):
            if i >= len(digits):
                res.append("".join(curr.copy()))
                return
            for j in range(len(vals[digits[i]])):
                curr.append(vals[digits[i]][j])
                backtrack(i+1, curr)
                curr.pop()
        backtrack(0, [])
        return res
            
