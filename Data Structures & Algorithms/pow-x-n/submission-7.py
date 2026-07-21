class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        abs_n = abs(n)
        base = x
        while abs_n:
            if abs_n & 1:
                res *= base
            base *= base
            abs_n >>= 1
        if n < 0:
            return 1 / res
        return res


