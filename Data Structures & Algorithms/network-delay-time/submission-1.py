class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for t in times:
            src, dest, time = t
            adj[src].append((time, dest))

        time = 0
        heap = [(0, k)]
        seen = set()
        while heap and len(seen) < n:
            curr = heapq.heappop(heap)
            t, src = curr[0], curr[1]
            time = max(time, t)
            for pair in adj[src]:
                weight, dest = pair[0], pair[1]
                if dest not in seen:
                    heapq.heappush(heap, (t + weight, dest))
            seen.add(src)

        return time if len(seen) == n else -1