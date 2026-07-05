class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adjList = defaultdict(list)

        for e in edges:
            sr, dst, wt = e
            adjList[sr].append((wt, dst))

        res = {}

        heap = [(0, src)]
        while heap:
            wt, node = heapq.heappop(heap)
            if node in res:
                continue
            res[node] = wt
            for nei in adjList[node]:
                curr_wt, to = nei
                if to in res:
                    continue
                heapq.heappush(heap, (wt + curr_wt, to))

        for i in range(n):
            if i not in res:
                res[i] = -1
        return res