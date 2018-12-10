class Solution(object):
  def increasingTriplet(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    a = b = float("inf")
    for num in nums:
      if num <= a:
        a = num
      elif num <= b:
        b = num
      else:
        return True
    return False
