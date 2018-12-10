class Solution(object):
  def findTargetSumWays(self, nums, S, visited={}, index=0):
    """
    :type nums: List[int]
    :type S: int
    :rtype: int
    """

    def helper(nums, S, visited={}, index=0):
      if (index, S) in visited:
        return visited[index, S]
      ans = 0
      if nums:
        ans += helper(nums[1:], S - nums[0], visited, index + 1)
        ans += helper(nums[1:], S + nums[0], visited, index + 1)
      elif S == 0:
        ans += 1
      visited[index, S] = ans
      return ans

    return helper(nums, S, {}, 0)
