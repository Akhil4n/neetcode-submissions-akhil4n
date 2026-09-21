class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = []
        time = 0
        heap = []
        if a > 0:
            heapq.heappush(heap, (a * -1, "a"))
        if b > 0:
            heapq.heappush(heap, (b * -1, "b"))
        if c > 0:
            heapq.heappush(heap, (c * -1, "c"))

        heapq.heapify(heap)
        queue = deque()

        while heap or queue:
            while queue and queue[0][1] <= time:
                val, chartime, char = queue.popleft()
                heapq.heappush(heap, (val, char))
            if not heap:
                break
            val, char = heapq.heappop(heap)
            res.append(char)
            if val == -1:
                time += 1
                continue
            if len(res) >= 2 and res[-1] == char and res[-2] == char:
                queue.append((val + 1, time + 2, char))
            else:
                heapq.heappush(heap, (val + 1, char))

            time += 1

        return "".join(res)

