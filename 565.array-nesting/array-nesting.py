class Solution(object):
  def arrayNesting(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    cache = [0] * len(nums)
    ans = 0
    for i, start in enumerate(nums):
      if cache[i]:
        continue
      p = start
      length = 1
      while nums[p] != start:
        cache[nums[p]] = 1
        p = nums[p]
        length += 1
      ans = max(ans, length)
    return ans
