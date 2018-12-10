class Solution(object):
  def splitArray(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    dp = [0] * (len(nums) + 1)
    for i in range(len(nums)):
      dp[i + 1] = dp[i] + nums[i]

    def split(start, end):
      return set(
        [dp[mid] - dp[start] for mid in range(start + 1, end) if dp[mid] - dp[start] == dp[end + 1] - dp[mid + 1]])

    return any(split(0, i - 1) & split(i + 1, len(nums) - 1) for i in range(3, len(nums) - 3))
