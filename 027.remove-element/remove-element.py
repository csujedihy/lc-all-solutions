class Solution(object):
  def removeElement(self, nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    slow = -1
    for i in range(0, len(nums)):
      if nums[i] != val:
        slow += 1
        nums[slow] = nums[i]
    return slow + 1
