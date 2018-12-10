# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
class IntvArray(object):
  def __init__(self):
    self._array = []
    self.append = lambda x: self._array.append(x)
    self.sort = self._array.sort

  def __len__(self):
    return len(self._array)

  def __getitem__(self, x):
    return self._array[x][0]

  def getIdx(self, x):
    if x >= len(self._array):
      return -1
    return self._array[x][1]


class Solution(object):
  def findRightInterval(self, intervals):
    """
    :type intervals: List[Interval]
    :rtype: List[int]
    """
    bst = IntvArray()
    ans = []
    for i, intv in enumerate(intervals):
      bst.append((intv.start, i))
    bst.sort()
    length = len(bst)
    for intv in intervals:
      idx = bisect.bisect_left(bst, intv.end)
      ans.append(bst.getIdx(idx))
    return ans
