import random


class Solution(object):
  def findKthLargest(self, nums, k):
    """
    :type A: List[int]
    :type k: int
    :rtype: int
    """

    def quickselect(start, end, nums, k):
      if start == end:
        return nums[start]

      mid = partition(start, end, nums)

      if mid == k:
        return nums[mid]
      elif k > mid:
        return quickselect(mid + 1, end, nums, k)
      else:
        return quickselect(start, mid - 1, nums, k)

    def partition(start, end, nums):
      p = random.randrange(start, end + 1)
      pv = nums[p]
      nums[end], nums[p] = nums[p], nums[end]
      mid = start
      for i in range(start, end):
        if nums[i] >= pv:
          nums[i], nums[mid] = nums[mid], nums[i]
          mid += 1
      nums[mid], nums[end] = nums[end], nums[mid]
      return mid

    ret = quickselect(0, len(nums) - 1, nums, k - 1)
    return ret

  def partition(start, end, nums):
    p = random.randrange(start, end + 1)
    pv = nums[p]
    nums[end], nums[p] = nums[p], nums[end]
    mid = start
    for i in range(start, end):
      if nums[i] >= pv:
        nums[i], nums[mid] = nums[mid], nums[i]
        mid += 1
    nums[mid], nums[end] = nums[end], nums[mid]
    return mid
