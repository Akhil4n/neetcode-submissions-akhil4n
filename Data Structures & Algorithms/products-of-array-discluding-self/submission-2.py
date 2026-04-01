class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        postfixProds = {}

        curr = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            postfixProds[i] = curr
            curr *= nums[i]

        res = []
        prefixProd = nums[0]
        for i in range(len(nums)):
            if i == 0:
                res.append(postfixProds[i])
            elif i == len(nums) - 1:
                res.append(prefixProd)
            else:
                res.append(postfixProds[i] * prefixProd)
                prefixProd *= nums[i]
        return res
