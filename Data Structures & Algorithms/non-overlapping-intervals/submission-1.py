class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        print(intervals)
        last = None
        res = 0
        for i, intvl in enumerate(intervals):
            if last is not None and intvl[0] < last[1]:
                if intvl[1] < last[1]:
                    last = intvl
                res += 1
            else:
                last = intvl
        return res

