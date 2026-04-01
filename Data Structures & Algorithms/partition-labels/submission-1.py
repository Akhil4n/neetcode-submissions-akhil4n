class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        farMap = {}
        for i in range(len(s)):
            curr = s[i]
            farMap[curr] = i

        start = end = 0
        for i, c in enumerate(s):
            end = max(end, farMap[c])
            if i == end:
                res.append(end - start + 1)
                start = i + 1
        
        return res



            