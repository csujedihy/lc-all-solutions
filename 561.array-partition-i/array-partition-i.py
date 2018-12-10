class Solution(object):
  def arrayPairSum(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    return sum([c for i, c in enumerate(sorted(nums)) if i % 2 == 0])
