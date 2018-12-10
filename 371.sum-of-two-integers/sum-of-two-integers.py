class Solution(object):
  def getSum(self, num1, num2):
    """
    :type a: int
    :type b: int
    :rtype: int
    """
    ans = 0
    mask = 0x01
    carry = 0
    for i in range(0, 32):
      a = num1 & mask
      b = num2 & mask
      c = carry
      carry = 0
      if a ^ b != 0:
        if c == 1:
          carry = 1
        else:
          ans |= mask
      else:
        if a & mask > 0:
          carry = 1
        if c == 1:
          ans |= mask

      mask = mask << 1
    if ans > 0x7fffffff:
      return ans - 0xffffffff - 1
    return ans
