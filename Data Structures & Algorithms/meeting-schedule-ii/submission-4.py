"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        res = 0

        intervals.sort(key=lambda x:x.start)

        heap = []

        for ivl in intervals:
            start = ivl.start
            end = ivl.end
            if not heap:
                res += 1
                heap.append(end)
            else:
                if heap[0] <= start:
                    heapq.heappop(heap)
                    heapq.heappush(heap, end)
                else:
                    res += 1
                    heapq.heappush(heap, end)
        return res