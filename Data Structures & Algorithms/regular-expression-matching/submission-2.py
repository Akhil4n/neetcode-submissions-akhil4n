class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        cache = {}

        def dfs(i, j):
            if j >= n and i >= m:
                return True
            if j >= n:
                return False
            if (i, j) in cache:
                return cache[(i, j)]

            match = i < m and (s[i] == p[j] or p[j] == '.')
            if j < n - 1 and p[j + 1] == "*":
                match = (match and (dfs(i + 1, j)) or dfs(i, j + 2))
            else:
                match = match and dfs(i + 1, j + 1)
            cache[(i, j)] = match
            return match
        return dfs(0, 0)