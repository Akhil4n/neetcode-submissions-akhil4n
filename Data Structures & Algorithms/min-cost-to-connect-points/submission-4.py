class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adjList = defaultdict(list)
        mst = {0: 0}

        for i, point in enumerate(points):
            for j in range(i, len(points)):
                xi, yi = point[0], point[1]
                xj, yj = points[j][0], points[j][1]
                dist = abs(xi - xj) + abs(yi - yj)
                adjList[i].append((dist, j))
                adjList[j].append((dist, i))

        heap = []
        for e in adjList[0]:
            heapq.heappush(heap, e)
        res = 0
        while heap:
            curr = heapq.heappop(heap)
            if curr[1] in mst:
                continue
            mst[curr[1]] = curr[0]
            res += curr[0]
            for e in adjList[curr[1]]:
                nei = e[1]
                if nei in mst:
                    continue
                heapq.heappush(heap, e)

        return res