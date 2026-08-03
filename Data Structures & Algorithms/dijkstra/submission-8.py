class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        res = {}
        adjList = defaultdict(list)
        for e in edges:
            frm, to, wgt = e
            adjList[frm].append((wgt, to))

        heap = []
        heap.append((0, src))

        while heap:
            wgt, node = heapq.heappop(heap)
            if node in res:
                continue
            res[node] = wgt
            for e in adjList[node]:
                curr_wt, curr_node = e
                if curr_node in res:
                    continue
                heapq.heappush(heap, (wgt + curr_wt, curr_node))

        for i in range(n):
            if i not in res:
                res[i] = -1
        return res