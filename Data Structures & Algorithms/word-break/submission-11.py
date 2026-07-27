class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        cache = {len(s): True}

        def dfs(i):
            if i in cache:
                return cache[i]

            for w in words:
                if s[i : i + len(w)] in words:
                    if dfs(i + len(w)):
                        cache[i] = True
                        return True
            cache[i] = False
            return False

        
        return dfs(0)




