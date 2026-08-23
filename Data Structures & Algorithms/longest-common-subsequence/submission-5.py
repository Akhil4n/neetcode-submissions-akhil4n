class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            short, long = text1, text2
        else:
            short, long = text2, text1

        dp = [[0 for _ in range(len(short))] for _ in range(len(long))]

        for i in range(len(long)):
            curr = long[i]
            for j in range(len(short)):
                if short[j] == curr:
                    diag = dp[i - 1][j - 1] if min(i - 1, j - 1) >= 0 else 0
                    dp[i][j] = 1 + diag
                else:
                    vert = dp[i - 1][j] if i - 1 >= 0 else 0
                    hor = dp[i][j - 1] if j - 1 >= 0 else 0
                    dp[i][j] = max(vert, hor)

        return dp[-1][-1]

