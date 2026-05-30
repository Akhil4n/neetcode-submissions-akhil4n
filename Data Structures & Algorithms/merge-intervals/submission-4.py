class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()

        check = None
        for intvl in intervals:
            if check is None:
                check = intvl
                continue
            if intvl[0] <= check[1]:
                check = [check[0], max(intvl[1], check[1])]
            else:
                res.append(check)
                check = intvl
        res.append(check)
        return res