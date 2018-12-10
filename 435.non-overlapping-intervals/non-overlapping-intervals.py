# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
  def eraseOverlapIntervals(self, intervals):
    """
    :type intervals: List[Interval]
    :rtype: int
    """
    intervals.sort(key=lambda i: i.end)
    ans = 0
    end = float("-inf")
    for interval in intervals:
      # print interval.start, interval.end
      if interval.start >= end:
        ans += 1
        end = interval.end
    return len(intervals) - ans
