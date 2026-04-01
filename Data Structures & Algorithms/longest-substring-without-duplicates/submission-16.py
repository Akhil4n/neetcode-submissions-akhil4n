class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, res = 0, 0
        freq = defaultdict(int)

        for r in range(len(s)):
            idxR = s[r]
            freq[idxR] += 1

            while freq[idxR] > 1:
                idxL = s[l]
                freq[idxL] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res