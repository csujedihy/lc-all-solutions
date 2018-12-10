class Solution(object):
  # better way
  def productExceptSelf(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
      dp[i] = dp[i - 1] * nums[i - 1]
    prod = 1
    for i in reversed(range(0, len(nums))):
      dp[i] = dp[i] * prod
      prod *= nums[i]
    return dp
