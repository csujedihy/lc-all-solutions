# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class SummaryRanges(object):

  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.intervals = []

  def insert(self, newInterval):
    """
    :type intervals: List[Interval]
    :type newInterval: Interval
    :rtype: List[Interval]
    """
    intervals = self.intervals
    # print intervals
    if not intervals:
      intervals.append(newInterval)
      return
    s, e = newInterval.start, newInterval.end
    left = filter(lambda x: x.end < newInterval.start, intervals)
    right = filter(lambda x: x.start > newInterval.end, intervals)
    # print left, right, (s, e)
    if left + right != intervals:
      s = min(intervals[len(left)].start, s)
      e = max(intervals[~len(right)].end, e)
    newIntv = Interval(s, e)
    if left and left[-1].end + 1 == s:
      newIntv.start = left[-1].start
      left = left[:-1]
    if right and right[0].start - 1 == e:
      newIntv.end = right[0].end
      right = right[1:]
    self.intervals = left + [newIntv] + right

  def addNum(self, val):
    """
    :type val: int
    :rtype: void
    """
    self.insert(Interval(val, val))

  def getIntervals(self):
    """
    :rtype: List[Interval]
    """
    return self.intervals

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
