class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        rows = len(s2) + 1
        cols = len(s1) + 1
        
        dp = [[False] * cols for _ in range(rows)]
        dp[0][0] = True

        for r in range(rows):
            for c in range(cols):
                if r == 0 and c == 0:
                    continue
                if r == 0:
                    dp[r][c] = (s1[c - 1] == s3[c - 1]) and (dp[r][c - 1])
                elif c == 0:
                    dp[r][c] = (s2[r - 1] == s3[r - 1]) and (dp[r - 1][c])
                else:
                    dp[r][c] = ((s1[c - 1] == s3[c + r - 1]) and (dp[r][c - 1])) or ((s2[r - 1] == s3[c + r - 1]) and dp[r - 1][c])

        return dp[-1][-1]