class Solution(object):
  def climbStairs(self, n):
    """
    :type n: int
    :rtype: int
    """
    if n <= 1:
      return 1
    pre, ppre = 1, 1
    for i in range(2, n + 1):
      tmp = pre
      pre = ppre + pre
      ppre = tmp
    return pre
