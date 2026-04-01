class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            while r + 1 - l - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r + 1 -l)
        return res
