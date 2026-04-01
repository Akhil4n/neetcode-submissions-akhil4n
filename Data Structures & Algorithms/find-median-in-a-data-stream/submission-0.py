class MedianFinder:

    def __init__(self):
        self.heap = []
        self.size = 0
    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap, num)
        self.size += 1
    def findMedian(self) -> float:
        vals = []
        if self.size % 2 != 0:
            for i in range(self.size // 2 + 1):
                vals.append(heapq.heappop(self.heap))
            res = vals[-1]
            for v in vals:
                heapq.heappush(self.heap, v)
            return res
        else:
            for i in range(self.size // 2 + 1):
                vals.append(heapq.heappop(self.heap))
            res = (vals[-1] + vals[-2]) / 2
            for v in vals:
                heapq.heappush(self.heap, v)
            return res