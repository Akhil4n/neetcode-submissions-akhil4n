class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        farMap = {}
        for i in range(len(s)):
            curr = s[i]
            farMap[curr] = i

        r = 0
        farthest = 0
        while r < len(s):
            start = r
            farthest = max(farthest, farMap[s[r]])
            if farthest == r:
                res.append(1)
                r = r + 1
                continue
            r2 = r
            while r2 < farthest:
                farthest = max(farthest, farMap[s[r2]])
                r2 += 1
            res.append(r2 - r + 1)
            r = r2 + 1
        return res


            