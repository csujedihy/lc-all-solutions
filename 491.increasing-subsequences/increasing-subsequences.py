class Solution(object):
  def findSubsequences(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    ans = []

    def dfs(nums, start, path, ans):
      if len(path) >= 2:
        ans.append(tuple(path + []))

      for i in range(start, len(nums)):
        if i != start and nums[i] == nums[i - 1]:
          continue
        if path and nums[i] < path[-1]:
          continue
        path.append(nums[i])
        dfs(nums, i + 1, path, ans)
        path.pop()

    dfs(nums, 0, [], ans)
    return list(set(ans))
