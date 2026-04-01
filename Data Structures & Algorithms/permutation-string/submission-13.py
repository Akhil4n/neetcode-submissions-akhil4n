class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) == 1:
            return s1 in s2
        l, r = 0, 1
        c = Counter(s1)
        while r < len(s2):
            if s2[l] not in c:
                l += 1
                r += 1
            elif s2[r] not in c:
                l = r + 1
                r = l + 1
            else:
                cc = Counter(s1)
                cc[s2[l]] -= 1
                while r < len(s2) and s2[r] in c and cc[s2[r]] > 0:
                    cc[s2[r]] -= 1
                    r += 1
                res = r - l
                if res == len(s1):
                    return True
                l += 1
                r = l + 1
                print(l, r)
        return False
