class Solution(object):
  def findMissingRanges(self, nums, lower, upper):
    """
    :type nums: List[int]
    :type lower: int
    :type upper: int
    :rtype: List[str]
    """
    ans = []
    nums = [lower - 1] + nums + [upper + 1]
    for i in range(0, len(nums) - 1):
      if nums[i] + 2 == nums[i + 1]:
        ans.append(str(nums[i] + 1))
      if nums[i + 1] > nums[i] + 2:
        ans.append(str(nums[i] + 1) + "->" + str(nums[i + 1] - 1))
    return ans
