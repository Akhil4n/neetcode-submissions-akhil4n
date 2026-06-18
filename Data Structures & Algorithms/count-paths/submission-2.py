class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for i in range(1, m):
            prev = 0
            for j in range(n):
                row[j] += prev 
                prev = row[j]
        return row[-1]