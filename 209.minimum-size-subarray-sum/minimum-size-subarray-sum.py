class Solution(object):
  def minSubArrayLen(self, target, nums):
    """
    :type target: int
    :type nums: List[int]
    :rtype: int
    """
    sum = 0
    j = 0
    ans = float("inf")
    for i in range(0, len(nums)):
      while j < len(nums) and sum < target:
        sum += nums[j]
        j += 1
      if sum >= target:
        ans = min(ans, j - i)
      sum -= nums[i]
    return ans if ans != float("inf") else 0
