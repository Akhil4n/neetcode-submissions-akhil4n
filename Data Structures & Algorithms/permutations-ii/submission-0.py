class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, curr = [], []

        def backtrack(seen):
            if len(seen) == len(nums):
                res.append(curr.copy())
                return
            i = 0
            for i in range(len(nums)):
                if i in seen:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and (i - 1) in seen:
                    continue

                seen.add(i)
                curr.append(nums[i])
                backtrack(seen)
                seen.remove(i)
                curr.pop()
                

        seen = set()
        backtrack(seen)
        return res
