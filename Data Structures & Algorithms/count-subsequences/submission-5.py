class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}

        def dfs(s_idx, t_idx):
            if t_idx >= len(t):
                return 1
            if s_idx >= len(s):
                return 0

            if (s_idx, t_idx) in cache:
                return cache[(s_idx, t_idx)]

            res = 0
            if s[s_idx] == t[t_idx]:
                res += dfs(s_idx + 1, t_idx + 1)
            res += dfs(s_idx + 1, t_idx)
            cache[(s_idx, t_idx)] = res
            return res

        return dfs(0, 0)