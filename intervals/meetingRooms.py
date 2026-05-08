"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals, key= lambda x: x.start)
        for i, interval in enumerate(intervals):
            end = interval.end
            r=i+1
            while r<=len(intervals)-1:
                r_interval_start = intervals[r].start
                if r_interval_start<end:
                    return False
                r+=1
            continue
        return True


