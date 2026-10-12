class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        p_s, p_e = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            curr_s, curr_e = intervals[i]
            if curr_s > p_e:
                res.append([p_s, p_e])
                p_s, p_e = curr_s, curr_e
            else:
                p_e = max(p_e, curr_e)
        res.append([p_s, p_e])
        return res