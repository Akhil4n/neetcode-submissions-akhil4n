class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        farMap = {}
        for ind, char in enumerate(s):
            farMap[char] = ind

        res = []
        curr_ind = 0
        while curr_ind < len(s):
            curr_char = s[curr_ind]
            end = farMap[curr_char]
            start = curr_ind
            while start < end:
                end = max(end, farMap[s[start]])
                start += 1
            res.append(end - curr_ind + 1)
            curr_ind = end + 1

        return res
                