from heapq import heappush, heappop
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        queue = deque()
        time = 0
        maxHeap = []

        for k, v in Counter(tasks).items():
            heapq.heappush(maxHeap, (-1 * v, k))
        
        while maxHeap or queue:
            if maxHeap:
                curr = heapq.heappop(maxHeap)
                val, task = curr[0] + 1, curr[1]
                if val < 0:
                    queue.append((time + n, val, task))
            if queue:
                if time >= queue[0][0]:
                    add = queue.popleft()
                    heapq.heappush(maxHeap, (add[1], add[2]))
            time += 1
        return time
