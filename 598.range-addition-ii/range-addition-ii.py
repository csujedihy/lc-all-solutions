class Solution(object):
  def maxCount(self, m, n, ops):
    """
    :type m: int
    :type n: int
    :type ops: List[List[int]]
    :rtype: int
    """
    return reduce(operator.mul, map(min, zip(*ops + [[m, n]])))
