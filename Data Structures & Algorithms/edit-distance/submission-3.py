class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}

        def dfs(idx1, idx2):

            if idx2 >= len(word2):
                return len(word1) - idx1
            if idx1 >= len(word1):
                return len(word2) - idx2

            if (idx1, idx2) in cache:
                return cache[(idx1, idx2)]

            res = 0
            if word1[idx1] == word2[idx2]:
                res = dfs(idx1 + 1, idx2 + 1)
            else:
                res = 1 + min(dfs(idx1 + 1, idx2), dfs(idx1, idx2 + 1), dfs(idx1 + 1, idx2 + 1))
            cache[(idx1, idx2)] = res
            return res

        return dfs(0, 0)