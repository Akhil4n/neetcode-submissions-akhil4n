class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProds = {}
        postfixProds = {}

        curr = nums[0]
        for i in range(1, len(nums)):
            prefixProds[i] = curr
            curr *= nums[i]

        curr = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            postfixProds[i] = curr
            curr *= nums[i]

        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(postfixProds[i])
            elif i == len(nums) - 1:
                res.append(prefixProds[i])
            else:
                res.append(postfixProds[i] * prefixProds[i])
        return res
