class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        def dfs():
            if len(sol) == len(nums):
                res.append(sol[:])
                return
            for n in nums:
                if n not in sol:
                    sol.append(n)
                    dfs()
                    sol.pop()
        dfs()
        return res
            