class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS = {}
        countT = {}
        for c in s:
            if c not in countS:
                countS[c] = 0
            countS[c] += 1
        for x in t:
            if x not in countT:
                countT[x] = 0
            countT[x] += 1
        return countS == countT