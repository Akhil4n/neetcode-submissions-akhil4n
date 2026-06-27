class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        res = 0
        seen = set()
        adjMap = defaultdict(list)

        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                md = abs(x1 - x2) + abs(y1 - y2)
                adjMap[i].append((md, j))
                adjMap[j].append((md, i))
        
        heap = [(0, 0)]
        while heap and len(seen) < len(points):
            curr = heapq.heappop(heap)
            md, dest = curr[0], curr[1]
            if dest in seen:
                continue
            res += md
            seen.add(dest)
            for nei in adjMap[dest]:
                wt, point = nei
                if point in seen:
                    continue
                heapq.heappush(heap, (wt, point))
        return res