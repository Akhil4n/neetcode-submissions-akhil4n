class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx, resLen = 0, 0

        for i, c in enumerate(s):
            if resLen == 0:
                resIdx, resLen = i, 1

            l, r = i - 1, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > resLen:
                    resLen = r - l + 1
                    resIdx = l
                l -= 1
                r += 1
            
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > resLen:
                    resLen = r - l + 1
                    resIdx = l
                l -= 1
                r += 1

        return s[resIdx: resIdx + resLen]