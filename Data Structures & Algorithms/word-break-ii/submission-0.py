class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res, curr = [], []

        def backtrack(i):
            if i >= len(s):
                res.append(" ".join(curr))
                return

            for word in wordDict:
                check = i + len(word)
                if check <= len(s) and s[i: check] == word:
                    curr.append(word)
                    backtrack(check)
                    curr.pop()

        backtrack(0)
        return res
                    