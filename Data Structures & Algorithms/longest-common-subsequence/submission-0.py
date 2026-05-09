class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
        rows = len(text1) - 1
        cols = len(text2) - 1

        for i in range(rows, -1, -1):
            t1char = text1[i]
            for j in range(cols, -1, -1):
                t2char = text2[j]
                if t1char == t2char:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        
        return dp[0][0]
