class Solution(object):
  def findMin(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ans = nums[0]
    start, end = 0, len(nums) - 1
    while start + 1 < end:
      mid = start + (end - start) / 2
      if nums[start] < nums[mid]:
        start = mid
      elif nums[start] > nums[mid]:
        end = mid
      else:
        start += 1
        ans = min(ans, nums[start])

    return min(ans, nums[start], nums[end])
