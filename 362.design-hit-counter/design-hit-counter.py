class HitCounter(object):

  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.q = [(0, 0)] * 300

  def hit(self, timestamp):
    """
    Record a hit.
    @param timestamp - The current timestamp (in seconds granularity).
    :type timestamp: int
    :rtype: void
    """
    idx = timestamp % 300
    time, hit = self.q[idx]
    if time != timestamp:
      self.q[idx] = timestamp, 1
    else:
      self.q[idx] = time, hit + 1

  def getHits(self, timestamp):
    """
    Return the number of hits in the past 5 minutes.
    @param timestamp - The current timestamp (in seconds granularity).
    :type timestamp: int
    :rtype: int
    """
    ans = 0
    for i in range(0, len(self.q)):
      time, hit = self.q[i]
      if timestamp - time < 300:
        ans += hit
    return ans

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
