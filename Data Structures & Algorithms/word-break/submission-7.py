class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        cache = {} # holds (start, end) -> bool

        def dfs(start, end):
            if end >= len(s):
                return s[start:end] in wordDict
            if (start, end) in cache:
                return cache[(start, end)]

            res = dfs(start, end + 1)
            if s[start:end] in wordDict:
                res = res or dfs(end, end + 1) 

            cache[(start, end)] = res
            return res
        
        return dfs(0, 0)




