class Solution(object):
  def findDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums) - 1
    start, end = 1, n
    while start + 1 < end:
      mid = start + (end - start) / 2
      count = 0
      for num in nums:
        if num < mid:
          count += 1
      if count >= mid:
        end = mid
      else:
        start = mid
    if nums.count(start) > nums.count(end):
      return start
    return end
