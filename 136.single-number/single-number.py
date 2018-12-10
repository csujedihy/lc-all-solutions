class Solution(object):
  def singleNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    for i in range(1, len(nums)):
      nums[0] ^= nums[i]
    return nums[0]
