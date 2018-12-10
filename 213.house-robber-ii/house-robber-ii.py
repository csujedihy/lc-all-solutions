class Solution(object):
  def rob(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0 or nums is None:
      return 0
    if len(nums) <= 2:
      return max(nums[:])
    # If we rob the first house, the problem becomes how to rob houses except the last one.
    # If we rob the last house, the problem becomes how to rob houses ecept the first one.
    return max(self.robHelper(nums[1:]), self.robHelper(nums[:len(nums) - 1]))

  def robHelper(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    pp = nums[0]
    p = max(pp, nums[1])
    for i in range(2, len(nums)):
      tmp = p
      p = max(pp + nums[i], p)
      pp = tmp
    return p
