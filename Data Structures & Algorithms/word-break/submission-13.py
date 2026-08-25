class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {}
        wordDict = set(wordDict)

        def dfs(start, end):
            if end >= len(s):
                return s[start:end] in wordDict
            if start in cache:
                return cache[start]

            curr = s[start: end + 1]
            res = False
            if curr in wordDict:
                res = dfs(end + 1, end + 1)
            if not res:
                res = res or dfs(start, end + 1)
            cache[start] = res
            return res

        res = dfs(0, 0)
        print(cache)
        return res

