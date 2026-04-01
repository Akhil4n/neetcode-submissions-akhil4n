class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def permute(curr, seen):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            for n in nums:
                if n not in seen:
                    seen.add(n)
                    curr.append(n)
                    permute(curr, seen)
                    seen.remove(n)
                    curr.pop()
        
        seen = set()
        permute([], seen)
        return res