class Solution(object):
  def findUnsortedSubarray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 2:
      return 0
    maxs = [float("inf")] * len(nums)
    mins = [float("inf")] * len(nums)
    mins[-1] = nums[-1]
    maxs[0] = nums[0]
    start, end = 0, -2
    for i in range(1, len(nums)):
      maxs[i] = max(maxs[i - 1], nums[i])
    for i in reversed(range(len(nums) - 1)):
      mins[i] = min(mins[i + 1], nums[i])
    for i in reversed(range(1, len(nums))):
      if nums[i] < maxs[i - 1]:
        end = i
        break
    for i in range(len(nums) - 1):
      if nums[i] > mins[i + 1]:
        start = i
        break
    print
    end, start
    return max(end - start + 1, 0)
