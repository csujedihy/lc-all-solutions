class Solution(object):
  def searchMatrix(self, matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """

    def binarySearch(nums, target):
      start, end = 0, len(nums) - 1
      while start + 1 < end:
        mid = start + (end - start) / 2
        if nums[mid] > target:
          end = mid
        elif nums[mid] < target:
          start = mid
        else:
          return True
      if nums[start] == target:
        return True
      if nums[end] == target:
        return True
      return False

    for nums in matrix:
      if binarySearch(nums, target):
        return True
    return False
