class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            new_n = 0
            while n > 0:
                dig = n % 10
                new_n += dig * dig
                n = n // 10
            if new_n in seen:
                return False
            seen.add(new_n)
            n = new_n
        return True