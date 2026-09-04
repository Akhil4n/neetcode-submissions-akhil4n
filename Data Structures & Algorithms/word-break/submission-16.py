class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in words:
                check = len(w) + i
                if check <= len(s) and s[i: check] == w:
                    dp[i] = dp[i] or dp[check]
        return dp[0]


        




