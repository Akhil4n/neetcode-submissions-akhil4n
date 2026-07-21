class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        res = []

        def processRow(r, c, dxn):
            if dxn == 'r':
                while c < cols and matrix[r][c] != 'X':
                    res.append(matrix[r][c])
                    matrix[r][c] = 'X'
                    c += 1
                if c >= cols or matrix[r][c] == 'X':
                    c -= 1
                if r + 1 >= rows or matrix[r + 1][c] == 'X':
                    return None
                return (r + 1, c, 'd')
            elif dxn == 'l':
                while c >= 0 and matrix[r][c] != 'X':
                    res.append(matrix[r][c])
                    matrix[r][c] = 'X'
                    c -= 1
                if c < 0 or matrix[r][c] == 'X':
                    c += 1
                if r - 1 < 0 or matrix[r - 1][c] == 'X':
                    return None
                return (r - 1, c, 'u')
        
        def processCol(r, c, dxn):
            if dxn == 'd':
                while r < rows and matrix[r][c] != 'X':
                    res.append(matrix[r][c])
                    matrix[r][c] = 'X'
                    r += 1
                if r >= rows or matrix[r][c] == 'X':
                    r -= 1
                if c - 1 < 0 or matrix[r][c - 1] == 'X':
                    return None
                return (r, c - 1, 'l')
            elif dxn == 'u':
                while r >= 0 and matrix[r][c] != 'X':
                    res.append(matrix[r][c])
                    matrix[r][c] = 'X'
                    r -= 1
                if r < 0 or matrix[r][c] == 'X':
                    r += 1
                if c + 1 >= cols or matrix[r][c + 1] == 'X':
                    return None
                return (r, c + 1, 'r')

        curr = (0, 0, 'r')
        while curr:
            curr = processRow(curr[0], curr[1], curr[2])
            if not curr:
                return res
            curr = processCol(curr[0], curr[1], curr[2])

        return res




