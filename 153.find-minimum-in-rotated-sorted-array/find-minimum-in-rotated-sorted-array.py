class Solution(object):
  def findMin(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    start, end, mid = 0, len(nums) - 1, 0
    while start + 1 < end:
      mid = start + (end - start) / 2
      if nums[start] <= nums[mid]:
        start = mid
      else:
        end = mid
    return min(nums[0], nums[start], nums[end])
