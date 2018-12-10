class Solution(object):
  def numWays(self, n, k):
    """
    :type n: int
    :type k: int
    :rtype: int
    """
    if n > 2 and k == 1:
      return 0
    if n < 2:
      return n * k
    pre = k * k
    ppre = k
    for i in range(2, n):
      tmp = pre
      pre = (k - 1) * (pre + ppre)
      ppre = tmp
    return pre
