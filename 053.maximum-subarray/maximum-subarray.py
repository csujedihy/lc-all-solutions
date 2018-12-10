class Solution(object):
  def maxSubArray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
      return 0
    preSum = maxSum = nums[0]
    for i in range(1, len(nums)):
      preSum = max(preSum + nums[i], nums[i])
      maxSum = max(maxSum, preSum)
    return maxSum
