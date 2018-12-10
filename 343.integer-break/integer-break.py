class Solution(object):
  def integerBreak(self, n):
    """
    :type n: int
    :rtype: int
    """
    if n <= 3:
      return n - 1
    if n % 3 == 0:
      return 3 ** (n / 3)
    if n % 3 == 1:
      return 3 ** ((n / 3) - 1) * 4
    if n % 3 == 2:
      return 3 ** (n / 3) * 2
