class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []

        intervals.sort()
        check = intervals[0]
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if curr[0] <= check[1]:
                check = [min(curr[0], check[0]), max(curr[1], check[1])]
            else:
                res.append(check)
                check = curr
        res.append(check)
        return res