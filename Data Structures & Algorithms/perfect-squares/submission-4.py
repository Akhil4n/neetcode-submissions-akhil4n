class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        square = 2
        while square * square <= n:
            squares.append(square * square)
            square += 1
        
        dp = [i for i in range(n + 1)]

        for square in squares:
            for i in range(n + 1):
                if i - square < 0:
                    continue
                dp[i] = min(dp[i], dp[i - square] + 1)

        return dp[-1]