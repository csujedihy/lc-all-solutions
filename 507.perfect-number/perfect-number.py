class Solution(object):
  def checkPerfectNumber(self, num):
    """
    :type num: int
    :rtype: bool
    """
    ans = 1
    div = 2
    while div ** 2 <= num:
      if num % div == 0:
        ans += div
        ans += num / div
      div += 1
    return ans == num if num != 1 else False
