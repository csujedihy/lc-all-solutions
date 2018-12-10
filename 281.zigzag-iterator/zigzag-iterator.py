from collections import deque


class ZigzagIterator(object):

  def __init__(self, v1, v2):
    """
    Initialize your data structure here.
    :type v1: List[int]
    :type v2: List[int]
    """
    self.iters = deque(map(iter, [v1, v2]))
    self.total = sum(map(len, [v1, v2]))

  def next(self):
    """
    :rtype: int
    """
    top = self.iters.popleft()
    try:
      value = top.next()
    except StopIteration:
      return self.next()
    self.total -= 1
    if self.total != 0:
      self.iters.append(top)
    return value

  def hasNext(self):
    """
    :rtype: bool
    """
    return self.total > 0

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
