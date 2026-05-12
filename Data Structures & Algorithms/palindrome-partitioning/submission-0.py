class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr = []

        def backtrack(start, curr):
            if start == len(s):
                res.append(curr.copy())
                return
            for end in range(start + 1, len(s) + 1):
                sub = s[start:end]
                if sub == sub[::-1]:
                    curr.append(sub)
                    backtrack(end, curr)
                    curr.pop()

        backtrack(0, curr)
        return res

            

            
        