class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1, n+1):
            adj[i] = []
        for t in times:
            src, dest, w = t
            adj[src].append([w, dest])
        
        visited = {}
        minHeap = []
        minHeap.append([0, k])
        while minHeap:
            wt1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                    continue
            visited[n1] = wt1
            for edge in adj[n1]:
                wt2, n2 = edge
                if n2 in visited:
                    continue
                heapq.heappush(minHeap, [wt1 + wt2, n2])
        return max(visited.values()) if len(visited) == n else -1

            
