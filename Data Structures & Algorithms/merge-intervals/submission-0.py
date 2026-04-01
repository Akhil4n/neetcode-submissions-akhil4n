class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return [intervals[0]]
        intervals.sort()
        res = []
        curr = intervals[0]
        for i in range(1, len(intervals)):
            intvl = intervals[i]
            if curr[1] >= intvl[0]:
                curr = [curr[0], max(intvl[1], curr[1])]
            else:
                res.append(curr)
                curr = intvl
        res.append(curr)
        return res