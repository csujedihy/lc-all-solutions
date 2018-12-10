class Solution(object):
  def isSelfCrossing(self, x):
    """
    :type x: List[int]
    :rtype: bool
    """
    if len(x) < 4:
      return False
    for i in range(3, len(x)):
      if x[i] >= x[i - 2] and x[i - 1] <= x[i - 3]:
        return True
      if i >= 4 and x[i - 1] == x[i - 3] and x[i] + x[i - 4] >= x[i - 2]:
        return True
      if i >= 5 and x[i - 1] <= x[i - 3] and x[i - 3] <= x[i - 1] + x[i - 5] and x[i] + x[i - 4] >= x[i - 2] and x[
        i - 4] <= x[i - 2]:
        return True
    return False
