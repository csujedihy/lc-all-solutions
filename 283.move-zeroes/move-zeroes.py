class Solution(object):
  def moveZeroes(self, nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    i = j = 0
    for i in range(0, len(nums)):
      if nums[i] != 0:
        nums[j], nums[i] = nums[i], nums[j]
        j += 1
