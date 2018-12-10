class Solution(object):
  def maxSubArrayLen(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    d = {0: -1}
    maxLen = 0
    _sum = 0
    for i in range(0, len(nums)):
      _sum += nums[i]
      if _sum not in d:
        d[_sum] = i
      if _sum - k in d:
        maxLen = max(maxLen, i - d[_sum - k])
    return maxLen
