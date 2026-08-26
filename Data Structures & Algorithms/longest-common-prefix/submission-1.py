class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []
        i = 0
        if len(strs[0]) == 0:
            return ""
        while i < len(strs[0]):
            curr = strs[0][i]
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != curr:
                    return "".join(res)
            res.append(curr)
            i += 1

        return "".join(res)

