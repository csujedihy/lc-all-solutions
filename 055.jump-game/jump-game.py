class Solution(object):
  def canJump(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    pos = 0
    bound = len(nums)
    while pos < len(nums) - 1:
      dis = nums[pos]
      if dis == 0:
        return False
      farthest = posToFarthest = 0
      for i in range(pos + 1, min(pos + dis + 1, bound)):
        canReach = i + nums[i]
        if i == len(nums) - 1:
          return True
        if canReach > farthest:
          farthest = canReach
          posToFarthest = i
      pos = posToFarthest
    return True if pos >= len(nums) - 1 else False
