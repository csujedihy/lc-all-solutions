class Solution(object):
  def findMinDifference(self, timePoints):
    """
    :type timePoints: List[str]
    :rtype: int
    """
    ans = 24 * 60
    times = [0] * len(timePoints)
    for i, time in enumerate(timePoints):
      h, m = map(int, time.split(":"))
      times[i] = h * 60 + m

    times.sort()

    for i in range(len(times) - 1):
      ans = min(ans, abs(times[i] - times[i + 1]))
    return min(ans, 1440 - abs(times[0] - times[-1]))
