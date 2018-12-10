class Solution(object):
  def combinationSum4(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    dp = [0] * (target + 1)
    dp[0] = 1

    for i in range(1, target + 1):
      for j in range(1, len(nums) + 1):
        if i - nums[j - 1] >= 0:
          dp[i] += dp[i - nums[j - 1]]
    return dp[-1]
