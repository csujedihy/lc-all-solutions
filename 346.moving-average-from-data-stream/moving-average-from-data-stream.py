from collections import deque


class MovingAverage(object):

  def __init__(self, size):
    """
    Initialize your data structure here.
    :type size: int
    """
    self.windowSize = size
    self.windowSum = 0.0
    self.data = deque([])

  def next(self, val):
    """
    :type val: int
    :rtype: float
    """
    self.windowSum += val
    data = self.data

    leftTop = 0
    if len(data) >= self.windowSize:
      leftTop = data.popleft()
    data.append(val)

    self.windowSum -= leftTop
    if len(data) < self.windowSize:
      return self.windowSum / len(data)
    return self.windowSum / self.windowSize

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
