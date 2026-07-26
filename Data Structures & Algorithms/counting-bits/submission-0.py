class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)

        curr = 1
        for i in range(1, n + 1):
            res[i] = curr.bit_count()
            curr += 1
        return res