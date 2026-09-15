class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)
        for ui, vi, ti in times:
            adjList[ui].append((vi, ti))
        
        heap = []
        heap.append((0, k))
        seen = set()
        res = 0
        while heap:
            curr = heapq.heappop(heap)
            time, ui = curr
            if ui in seen:
                continue
            res = time
            seen.add(ui)
            for vi, ti in adjList[ui]:
                if vi in seen:
                    continue
                else:
                    heapq.heappush(heap, (time + ti, vi))
        return res if len(seen) == n else -1