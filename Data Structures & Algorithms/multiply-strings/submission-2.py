class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        number1 = number2 = 0

        for i in range(len(num1)):
            curr = ord(num1[i]) - ord('0')
            number1 *= 10
            number1 += curr
        for i in range(len(num2)):
            curr = ord(num2[i]) - ord('0')
            number2 *= 10
            number2 += curr

        print(number1, number2)
        if number1 == 0 or number2 == 0:
            return "0"
        mult_int = number1 * number2
        res = deque()
        while mult_int > 0:
            dig = mult_int % 10
            res.appendleft(chr(ord('0') + dig))
            mult_int = mult_int // 10
        return "".join(res)
