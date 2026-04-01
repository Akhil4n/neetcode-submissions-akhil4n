class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0

        seen = {}
        l, r = 0, 0
        for r in range(len(s)):
            val = s[r]
            if val in seen:
                l = max(l, seen[val] + 1)
            seen[val] = r
            print(l, r)
            res = max(res, r - l + 1)

        return res