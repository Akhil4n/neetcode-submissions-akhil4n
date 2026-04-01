class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        postfixProds = {}

        curr = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            postfixProds[i] = curr
            curr *= nums[i]

        res = []
        prefixProd = 1
        for i in range(len(nums)):
            postfix = postfixProds.get(i, 1)
            res.append(prefixProd * postfix)
            prefixProd *= nums[i]
        return res
