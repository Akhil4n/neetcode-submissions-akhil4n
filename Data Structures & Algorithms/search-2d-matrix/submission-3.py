class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        oL, oR = 0, len(matrix) - 1
        
        # Binary search to find the row
        while oL <= oR:
            oM = (oL + oR) // 2
            row = matrix[oM]
            
            if row[0] <= target <= row[-1]:
                break
            elif target < row[0]:
                oR = oM - 1
            else:
                oL = oM + 1
        
        if oL > oR:
            return False
        
        # Binary search inside the row
        row = matrix[oM]
        iL, iR = 0, len(row) - 1
        
        while iL <= iR:
            iM = (iL + iR) // 2
            if row[iM] == target:
                return True
            elif row[iM] < target:
                iL = iM + 1
            else:
                iR = iM - 1
        
        return False
