class Solution(object):
  def trailingZeroes(self, n):
    """
    :type n: int
    :rtype: int
    """
    count, k = 0, 5
    while n:
      k = n / 5
      count += k
      n = k
    return count
