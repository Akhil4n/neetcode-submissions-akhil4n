class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        r = 0
        res = []
        dque = deque()

        while r < len(nums):
            while dque and nums[dque[-1]] < nums[r]:
                dque.pop()
            dque.append(r)

            if dque[0] < r - k + 1:
                dque.popleft()
            
            if r >= k - 1:
                res.append(nums[dque[0]])
            r += 1
        return res