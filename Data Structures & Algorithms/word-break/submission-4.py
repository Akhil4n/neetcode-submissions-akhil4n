class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {}
        wordDict = set(wordDict)

        def dfs(start, end):
            if start == end == len(s):
                return True

            if end >= len(s):
                return False

            if (start, end) in cache:
                return cache[(start, end)]

            res = False
            if s[start:end+1] in wordDict:
                res = dfs(end + 1, end + 1)

            res |= dfs(start, end + 1)

            cache[(start, end)] = res
            return res
            
        return dfs(0, 0)