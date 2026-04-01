from heapq import heapify, heappush, heappop
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.nums = []
        self.k = k
        heapify(self.nums)
        for n in nums:
            heappush(self.nums, n)
            if len(self.nums) > k:
                heappop(self.nums)
    
    def add(self, val: int) -> int:
        heappush(self.nums, val)
        if len(self.nums) > self.k:
            heappop(self.nums)
        return self.nums[0]
