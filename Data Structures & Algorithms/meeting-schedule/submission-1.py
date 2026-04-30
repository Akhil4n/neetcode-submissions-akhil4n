"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        if not intervals:
            return True
        intervals.sort(key=lambda x:x.start)

        start, end = intervals[0].start, intervals[0].end

        for i in range(1, len(intervals)):
            cS, cE = intervals[i].start, intervals[i].end

            if cS < end:
                return False

            start, end = cS, cE

        return True