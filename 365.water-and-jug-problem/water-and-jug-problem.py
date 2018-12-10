class Solution(object):
  def canMeasureWater(self, x, y, z):
    """
    :type x: int
    :type y: int
    :type z: int
    :rtype: bool
    """
    if z > x + y:
      return False
    if z == 0:
      return True
    if x == z or y == z or x + y == z:
      return True
    if min(x, y) == 0:
      return True if max(x, y) == z else False
    n = min(x, y)
    while n > 1:
      if x % n == 0 and y % n == 0:
        break
      n -= 1
    if z % n == 0:
      return True
    return False
