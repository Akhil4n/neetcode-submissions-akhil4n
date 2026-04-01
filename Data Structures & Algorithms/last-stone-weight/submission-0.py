from heapq import heapify, heappop, heappush
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for s in stones:
            heappush(heap, -1 * s)
        while len(heap) > 1:
            stone1 = abs(heappop(heap))
            stone2 = abs(heappop(heap))
            if stone1 == stone2:
                continue
            elif stone1 > stone2:
                heappush(heap, (stone1 - stone2) * -1)
            elif stone2 > stone1:
                heappush(heap, (stone2 - stone1) * -1)
        if heap:
            return abs(heap[0])
        return 0