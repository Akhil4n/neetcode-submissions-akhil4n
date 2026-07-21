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
                return mult(split) * mult(split)
            else:
                return mult(split + 1) * mult(split)

        res = mult(abs(n))
        if n < 0:
            return 1 / res
        return res
