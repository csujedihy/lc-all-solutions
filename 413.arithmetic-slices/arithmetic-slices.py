class Solution(object):
  def numberOfArithmeticSlices(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ans = 0
    if len(nums) > 2:
      diff = [nums[i] - nums[i - 1] for i in range(1, len(nums))]
      count = 1
      pre = diff[0]
      for i in range(1, len(diff)):
        if diff[i] == pre:
          count += 1
        else:
          ans += count * (count - 1) / 2
          count = 1
        pre = diff[i]
      ans += count * (count - 1) / 2
    return ans
