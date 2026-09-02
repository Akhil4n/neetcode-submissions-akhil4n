class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {}

        def backtrack(i):
            if i in memo:
                return memo[i]

            if i >= len(s):
                return [[]]

            res = []
            for word in wordDict:
                check = i + len(word)
                if check <= len(s) and s[i: check] == word:
                    for rest in backtrack(check):
                        res.append([word] + rest)

            memo[i] = res
            return res

        partitions = backtrack(0)
        return [" ".join(partition) for partition in partitions]
                    