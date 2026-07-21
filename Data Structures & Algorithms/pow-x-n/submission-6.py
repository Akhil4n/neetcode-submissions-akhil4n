class Solution:
    def myPow(self, x: float, n: int) -> float:
        cache = {}

        def mult(n):
            if n == 0:
                return 1
            
            if n in cache:
                return cache[n]
            split = n // 2

            half = mult(split)
            if n % 2 == 0:
                res = half * half
            else:
                res = half * half * x
            cache[n] = res
            return res
        res = mult(abs(n))
        if n < 0:
            return 1 / res
        return res
