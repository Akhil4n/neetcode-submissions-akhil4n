class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        for r in range(rows):
            found = False
            for c in range(cols):
                if matrix[r][c] == 0:
                    found = True
                    break
            if found:
                for c in range(cols):
                    if matrix[r][c] != 0:
                        matrix[r][c] = "X"
        
        for c in range(cols):
            found = False
            for r in range(rows):
                if matrix[r][c] == 0:
                    found = True
                    break
            if found:
                for r in range(rows):
                    if matrix[r][c] != 0:
                        matrix[r][c] = "X"

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == "X":
                    matrix[r][c] = 0
                    

        