class Solution(object):
  def optimalDivision(self, nums):
    """
    :type nums: List[int]
    :rtype: str
    """
    if len(nums) < 3:
      return "/".join(map(str, nums))
    return "%s/(%s)" % (nums[0], "/".join(map(str, nums[1:])))
