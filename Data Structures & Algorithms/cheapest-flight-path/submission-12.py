class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float('inf')] * n
        dist[src] = 0

        for _ in range(k + 1):
            new_vals = {}
            for frm, to, w in flights:
                if dist[to] > dist[frm] + w:
                    if to not in new_vals:
                        new_vals[to] = dist[frm] + w
                    else:
                        new_vals[to] = min(new_vals[to], dist[frm] + w)

            for idx, val in new_vals.items():
                dist[idx] = val
        return dist[dst] if dist[dst] < float('inf') else -1