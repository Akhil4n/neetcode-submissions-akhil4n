class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []

        target = math.floor(len(nums) / 3)

        count = Counter(nums)
        for val in count:
            if count[val] > target:
                res.append(val)
        return res
