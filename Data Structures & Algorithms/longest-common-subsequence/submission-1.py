class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) <= len(text2):
            colStr, rowStr = text1, text2
        else:
            colStr, rowStr = text2, text1
        
        currRow = [0] * len(colStr)

        for r in range(len(rowStr)):
            newRow = [0] * len(colStr)
            for c in range(len(colStr)):
                if rowStr[r] != colStr[c]:
                    val1 = currRow[c]
                    val2 = newRow[c - 1] if c - 1 >= 0 else 0
                    newRow[c] = max(val1, val2)
                else:
                    diagVal = currRow[c - 1] + 1 if c - 1 >= 0 else 1
                    newRow[c] = diagVal
            currRow = newRow
        return currRow[-1]