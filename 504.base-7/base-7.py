class Solution(object):
  def convertToBase7(self, num):
    """
    :type num: int
    :rtype: str
    """

    def convertHelper(num, base):
      sign = ""
      if num < 0:
        sign = "-"
      num = abs(num)
      ans = 0
      unit = 1
      while num:
        ans += (num % base) * unit
        num /= base
        unit *= 10
      return sign + str(ans)

    return convertHelper(num, 7)
