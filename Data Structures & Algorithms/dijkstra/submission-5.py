class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        res = {}

        adjMap = defaultdict(list)
        for sorc, dst, weight in edges:
            adjMap[sorc].append((weight, dst))
        
        heap = [(0, src)]

        while len(heap) > 0 and len(res) < n:
            weight, curr = heapq.heappop(heap)
            if curr in res:
                continue

            res[curr] = weight

            for nei in adjMap[curr]:
                if nei[1] in res:
                    continue
                new_weight = weight + nei[0]
                heapq.heappush(heap, (new_weight, nei[1]))

        for i in range(n):
            if i not in res:
                res[i] = -1
        return res