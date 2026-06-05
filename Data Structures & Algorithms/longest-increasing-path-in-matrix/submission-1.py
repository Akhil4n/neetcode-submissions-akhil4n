class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        memo = {}

        def dfs(i, j, prev):
            if min(i, j) < 0 or i >= rows or j >= cols or matrix[i][j] <= prev:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            res = 1 + max(dfs(i + 1, j, matrix[i][j]), dfs(i - 1, j, matrix[i][j]), 
                        dfs(i, j - 1, matrix[i][j]), dfs(i, j + 1, matrix[i][j]))
            memo[(i, j)] = res
            return res

        res = 0
        for r in range(rows):
            for c in range(cols):
                res = max(res, dfs(r, c, float('-inf')))
        return res