class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            seen = set()
            j = i
            while j < len(s) and s[j] not in seen:
                seen.add(s[j])
                j += 1
            res = max(res, len(seen))
        return res