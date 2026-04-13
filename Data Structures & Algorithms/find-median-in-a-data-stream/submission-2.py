class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []
    
    def addNum(self, num: int) -> None:
        if len(self.maxheap) >= len(self.minheap) + 1:
            heapq.heappush(self.minheap, num)
        else:
            heapq.heappush(self.maxheap, num * -1)
        if self.minheap and self.minheap[0] < self.maxheap[0] * -1:
            num1 = heapq.heappop(self.minheap)
            num2 = -1 * heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, num2)
            heapq.heappush(self.maxheap, num1 * -1)

    def findMedian(self) -> float:
        if (len(self.maxheap) + len(self.minheap)) % 2 == 0:
            num1 = -1 * self.maxheap[0]
            num2 = self.minheap[0]
            return (num1 + num2) / 2
        else:
            res = -1 * self.maxheap[0]
            return res