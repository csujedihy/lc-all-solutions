class Solution(object):
  def singleNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    xor = 0
    for num in nums:
      xor ^= num

    xor = xor & -xor
    a, b = 0, 0
    for num in nums:
      if num & xor:
        a ^= num
      else:
        b ^= num

    return a, b
