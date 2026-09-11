class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x:x[1])
        heap = [] # stores drop off, num
        currpos = currcap = 0
        for numpass, frm, to in trips:
            while heap and heap[0][0] <= frm:
                dropoff = heapq.heappop(heap)[1]
                currcap -= dropoff
            currcap += numpass
            if currcap > capacity:
                return False
            heapq.heappush(heap, (to, numpass))

        return True