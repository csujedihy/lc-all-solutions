class Solution(object):
  def findDisappearedNumbers(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    ans = []
    for i in range(0, len(nums)):
      idx = abs(nums[i]) - 1
      nums[idx] = -nums[idx] if nums[idx] > 0 else nums[idx]

    for i in range(0, len(nums)):
      if nums[i] > 0:
        ans.append(i + 1)

    for i in range(0, len(nums)):
      nums[idx] = -nums[idx] if nums[idx] < 0 else nums[idx]
    return ans
