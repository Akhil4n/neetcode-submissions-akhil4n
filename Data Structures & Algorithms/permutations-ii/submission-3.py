class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res, curr = [], []
        count = Counter(nums)

        def backtrack():
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for num in count:
                if count[num] == 0:
                    continue

                count[num] -= 1
                curr.append(num)
                backtrack()
                count[num] += 1
                curr.pop()
                
        backtrack()
        return res
