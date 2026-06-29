class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjMap = defaultdict(list)
        for f in flights:
            frm, to, time = f
            adjMap[frm].append((time, to))
        
        res = float('inf') 
        heap = []
        heapq.heappush(heap, ((0, src, 0)))
        seen = {}
        while heap:
            curr = heapq.heappop(heap)
            if curr[2] > k + 1 or (curr[1] in seen and seen[curr[1]] < curr[2]):
                continue
            currTime = curr[0]
            if curr[1] == dst:
                return currTime
            seen[curr[1]] = curr[2]
            for nei in adjMap[curr[1]]:
                if nei[1] not in seen:
                    heapq.heappush(heap,(currTime + nei[0], nei[1], curr[2] + 1))
            
        return -1 if res == float('inf') else res