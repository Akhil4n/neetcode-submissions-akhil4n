class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        res = 1
        rows, cols = len(matrix), len(matrix[0])
        cache = {}

        def dfs(r, c, val):
            if min(r, c) < 0 or r >= rows or c >= cols or matrix[r][c] <= val:
                return 0
            if (r, c) in cache:
                return cache[(r, c)]

            res = 1 + max(dfs(r + 1, c, matrix[r][c]), dfs(r - 1, c, matrix[r][c]), dfs(r, c + 1, matrix[r][c]),
                        dfs(r, c - 1, matrix[r][c]))

            cache[(r, c)] = res
            return res

        for r in range(rows):
            for c in range(cols):
                res = max(res, dfs(r, c, float('-inf')))

        return res
