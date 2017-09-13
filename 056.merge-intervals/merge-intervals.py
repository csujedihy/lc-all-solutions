# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        ans = []
        for intv in sorted(intervals, key=lambda x:x.start):
            if ans and ans[-1].end >= intv.start:
                ans[-1].end = max(ans[-1].end, intv.end)
            else:
                ans.append(intv)
        return ans