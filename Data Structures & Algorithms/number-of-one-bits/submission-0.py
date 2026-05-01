class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        for i in range(32):
            curPow = 31 - i
            check = 2 ** curPow
            if check > n:
                continue
            else:
                n -= check
                res += 1

        return res