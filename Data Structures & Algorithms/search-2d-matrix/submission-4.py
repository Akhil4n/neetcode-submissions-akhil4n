class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        oL, oR = 0, len(matrix) - 1
        while oL <= oR:
            oM = (oL + oR) // 2
            curr = matrix[oM]

            if target < curr[0]:
                oR = oM - 1
            elif target > curr[-1]:
                oL = oM + 1
            else:
                break
        if oL > oR:
            return False
        curr = matrix[oM]
        iL, iR = 0, len(curr) - 1
        while iL <= iR:
            iM = (iL + iR) // 2
            key = curr[iM]
            if key == target:
                return True
            elif key > target:
                iR = iM - 1
            else:
                iL = iM + 1
        return False