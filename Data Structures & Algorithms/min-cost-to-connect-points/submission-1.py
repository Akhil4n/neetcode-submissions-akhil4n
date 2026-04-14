class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = []
        mst = set()
        res = 0
        
        start = points[0]
        for i in range(1, len(points)):
            curr = points[i]
            dist = abs(start[0] - curr[0]) + abs(start[1] - curr[1])
            heapq.heappush(heap, (dist, 0, i))
        mst.add(0)
            
        while heap and len(mst) < len(points):
            dist, u, v = heapq.heappop(heap)
            if v in mst:
                continue
            res += dist
            start = points[v]
            for i in range(len(points)):
                if i != v and i not in mst:
                    curr = points[i]
                    dist = abs(start[0] - curr[0]) + abs(start[1] - curr[1])
                    heapq.heappush(heap, (dist, v, i))
            mst.add(v)
        
        return res