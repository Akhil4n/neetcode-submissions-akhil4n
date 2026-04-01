from heapq import heapify, heappop, heappush
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        heap = []
        for p in points:
            dist = math.sqrt((p[0] ** 2) + (p[1] ** 2))
            heap_val = (-1 * dist, p[0], p[1])
            heappush(heap, heap_val)
            if len(heap) > k:
                heappop(heap)
        while len(heap) > 0:
            cur = heappop(heap)
            res.append([cur[1], cur[2]])
        return res
            