class Solution(object):
  # normal way
  def _isPalindrome(self, x):
    """
    :type x: int
    :rtype: bool
    """
    z = x
    y = 0
    while x > 0:
      y = y * 10 + x % 10
      x /= 10
    return z == y

  # faster way
  def isPalindrome(self, x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0 or (x != 0 and x % 10 == 0):
      return False
    half = 0
    while x > half:
      half = half * 10 + x % 10
      x /= 10
    return x == half or half / 10 == x
