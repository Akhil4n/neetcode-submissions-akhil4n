class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) <= len(text2):
            colStr, rowStr = text1, text2
        else:
            colStr, rowStr = text2, text1
        
        currRow = [0] * len(colStr)
        prevDiag = 0

        for r in range(len(rowStr)):
            for c in range(len(colStr)):
                if rowStr[r] != colStr[c]:
                    prevDiag = currRow[c] if c < len(colStr) - 1 else 0
                    val1 = currRow[c]
                    val2 = currRow[c - 1] if c - 1 >= 0 else 0
                    currRow[c] = max(val1, val2)
                else:
                    diagVal = prevDiag + 1
                    prevDiag = currRow[c] if c < len(colStr) - 1 else 0
                    currRow[c] = diagVal
        return currRow[-1]