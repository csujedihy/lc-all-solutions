class Solution(object):
  def addDigits(self, num):
    """
    :type num: int
    :rtype: int
    """
    if num < 10:
      return num
    return 1 + (num - 1) % 9
