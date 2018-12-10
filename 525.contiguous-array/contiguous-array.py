class Solution(object):
  def findMaxLength(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    d = {0: -1}
    count = ans = 0
    delta = {1: -1, 0: 1}
    for i in range(len(nums)):
      count += delta.get(nums[i], 0)
      if count in d:
        ans = max(ans, i - d[count])
      else:
        d[count] = i
    return ans
