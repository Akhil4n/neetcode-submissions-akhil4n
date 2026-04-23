class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adjList = defaultdict(list)
        for t in times:
            src, dest, weight = t
            adjList[src].append((weight, dest))

        heap = []
        seen = set()
        heap.append((0, k))

        while heap:
            weight, node = heapq.heappop(heap)
            if node in seen:
                continue
            seen.add(node)
            if len(seen) == n:
                return weight
            
            for e in adjList[node]:
                w, dest = e
                if dest in seen:
                    continue
                heapq.heappush(heap, (weight + w, dest))
                

        return -1
            
