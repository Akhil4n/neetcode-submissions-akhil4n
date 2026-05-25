class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        used = set()
        def backtrack(i, curr):
            if i >= len(nums):
                res.append(curr.copy())
                return
            for n in nums:
                if n not in used:
                    used.add(n)
                    curr.append(n)
                    backtrack(i+1, curr)
                    curr.pop()
                    used.remove(n)
            
        backtrack(0, [])
        return res