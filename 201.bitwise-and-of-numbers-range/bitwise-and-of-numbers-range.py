class Solution(object):
  def rangeBitwiseAnd(self, m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    while m < n:
      n = n & n - 1
    return n
