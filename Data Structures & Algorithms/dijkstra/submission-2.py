class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {}
        for i in range(n):
            adj[i] = []
        for e in edges:
            s, dst, wt = e
            adj[s].append([wt, dst])
        visited = {}
        minHeap = []
        minHeap.append([0, src])
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited[n1] = w1
            for edge in adj[n1]:
                w2, n2 = edge
                if n2 not in visited:
                    heapq.heappush(minHeap, [w1 + w2, n2])
        for i in range(n):
            if i not in visited:
                visited[i] = -1
        return visited