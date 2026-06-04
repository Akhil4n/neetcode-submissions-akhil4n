class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        heap = []
        for intvl in intervals:
            heapq.heappush(heap, (intvl[0], intvl[1]))
        res = []
        for q in queries:
            intvl_len = float('inf')
            popped = []
            while heap and q >= heap[0][0]:
                curr = heapq.heappop(heap)
                popped.append(curr)
                if q <= curr[1]:
                    intvl_len = min(intvl_len, curr[1] - curr[0] + 1)
            for p in popped:
                heapq.heappush(heap, p)
            if intvl_len == float('inf'):
                intvl_len = -1
            res.append(intvl_len)
        return res