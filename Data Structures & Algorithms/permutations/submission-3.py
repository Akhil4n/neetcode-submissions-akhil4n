class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        numset = set(nums)
        def backtrack(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            for num in numset:
                if num not in curr:
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()

        backtrack([])
        return res
            

