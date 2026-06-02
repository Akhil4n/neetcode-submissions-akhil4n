class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = defaultdict(list)
        for e in edges:
            adj[e[0]].append((e[1], e[2]))

        res = {}
        heap = []
        heap.append((0, src))

        while heap:
            weight, curr = heapq.heappop(heap)
            if curr in res:
                continue
            res[curr] = weight
            for e in adj[curr]:
                dest = e[0]
                add_weight = weight + e[1]
                heapq.heappush(heap, (add_weight, dest))

        for i in range(n):
            if i not in res:
                res[i] = -1
        return res