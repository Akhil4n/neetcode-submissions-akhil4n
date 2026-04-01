class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for p in points:
            x, y = p[0], p[1]
            dist = x**2 + y**2
            heapelement = (-1 * dist, x, y)
            if len(maxHeap) < k:
                heapq.heappush(maxHeap, heapelement)
            else:
                if dist < -1 * maxHeap[0][0]:
                    heapq.heappop(maxHeap)
                    heapq.heappush(maxHeap, heapelement)
        res = []
        for el in maxHeap:
            res.append([el[1], el[2]])
        return res
            