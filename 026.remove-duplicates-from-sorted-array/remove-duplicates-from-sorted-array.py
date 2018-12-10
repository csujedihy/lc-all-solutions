class Solution(object):
  def removeDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) <= 1:
      return len(nums)
    slow = 0
    for i in range(1, len(nums)):
      if nums[i] != nums[slow]:
        slow += 1
        nums[slow] = nums[i]
    return slow + 1
