class Solution:
    def myPow(self, x: float, n: int) -> float:
        cache = {1: x}

        def mult(n):
            if n == 0:
                return 1
            
            if n in cache:
                return cache[n]
            split = n // 2
            if n % 2 == 0:
                res = mult(split) * mult(split)
            else:
                res = mult(split) * mult(split) * mult(1)
            cache[n] = res
            return res
        res = mult(abs(n))
        if n < 0:
            return 1 / res
        return res
