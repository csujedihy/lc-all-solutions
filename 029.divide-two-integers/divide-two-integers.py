class Solution(object):
  def divide(self, dividend, divisor):
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    """
    if divisor == 0:
      return 0x7fffffff
    sign = 1
    if dividend * divisor < 0:
      sign = -1
    ans = 0
    cnt = 1
    dividend = abs(dividend)
    divisor = abs(divisor)
    subsum = divisor
    while dividend >= divisor:
      while (subsum << 1) <= dividend:
        cnt <<= 1
        subsum <<= 1
      ans += cnt
      cnt = 1
      dividend -= subsum
      subsum = divisor
    return max(min(sign * ans, 0x7fffffff), -2147483648)
