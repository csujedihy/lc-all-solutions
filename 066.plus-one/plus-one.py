class Solution(object):
  def plusOne(self, digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    carry = 1
    for i in reversed(range(0, len(digits))):
      digit = (digits[i] + carry) % 10
      carry = 1 if digit < digits[i] else 0
      digits[i] = digit
    if carry == 1:
      return [1] + digits
    return digits
