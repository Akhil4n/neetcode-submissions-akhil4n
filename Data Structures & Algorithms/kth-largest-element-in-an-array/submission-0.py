from heapq import heapify, heappop, heappush
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapify(heap)
        for n in nums:
            heappush(heap, n)
            if len(heap) > k:
                heappop(heap)
        return heap[0]