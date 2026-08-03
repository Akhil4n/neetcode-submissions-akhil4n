class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, curr = [], []

        def backtrack(i):
            if len(curr) == k:
                res.append(curr.copy())
                return
            need = k - len(curr)
            remaining = n - i + 1
            if remaining < need:
                return
            for num in range(i, n + 1):
                curr.append(num)
                backtrack(num + 1)
                curr.pop()

        backtrack(1)
        return res