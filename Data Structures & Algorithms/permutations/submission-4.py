class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = set()

        def backtrack(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for i in range(len(nums)):
                if i in used:
                    continue

                used.add(i)
                curr.append(nums[i])

                backtrack(curr)

                used.remove(i)
                curr.pop()
                

        backtrack([])
        return res