class Solution(object):
  def jump(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    pos = 0
    ans = 0
    bound = len(nums)
    while pos < len(nums) - 1:
      dis = nums[pos]
      farthest = posToFarthest = 0
      for i in range(pos + 1, min(pos + dis + 1, bound)):
        canReach = i + nums[i]
        if i == len(nums) - 1:
          return ans + 1
        if canReach > farthest:
          farthest = canReach
          posToFarthest = i
      ans += 1
      pos = posToFarthest
    return ans
