class Solution(object):
  def sortColors(self, nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    x = y = z = -1
    for i in range(0, len(nums)):
      if nums[i] == 0:
        x += 1
        y += 1
        z += 1
        if z != -1:
          nums[z] = 2
        if y != -1:
          nums[y] = 1
        nums[x] = 0
      elif nums[i] == 1:
        y += 1
        z += 1
        nums[z] = 2
        if x != -1:
          nums[x] = 0
        if y != -1:
          nums[y] = 1
      elif nums[i] == 2:
        z += 1
        if y != -1:
          nums[y] = 1
        if x != -1:
          nums[x] = 0
        nums[z] = 2
