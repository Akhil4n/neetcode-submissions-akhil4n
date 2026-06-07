class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = defaultdict(int)

        def dfs(s_ind, t_ind):
            if (s_ind, t_ind) in cache:
                return cache[(s_ind, t_ind)]
            if t_ind >= len(t):
                return 1
            if s_ind >= len(s):
                return 0
            if len(s) - s_ind < len(t) - t_ind:
                return 0
            res = 0
            if s[s_ind] == t[t_ind]:
                res += dfs(s_ind + 1, t_ind + 1)
            res += dfs(s_ind + 1, t_ind)
            cache[(s_ind, t_ind)] = res
            return res
        
        return dfs(0, 0)