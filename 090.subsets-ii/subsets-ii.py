class Solution(object):
  def subsetsWithDup(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    def dfs(start, nums, path, res, visited):
      res.append(path + [])

      for i in range(start, len(nums)):
        if start != i and nums[i] == nums[i - 1]:
          continue
        if i not in visited:
          visited[i] = 1
          path.append(nums[i])
          dfs(i + 1, nums, path, res, visited)
          path.pop()
          del visited[i]

    nums.sort()
    res = []
    visited = {}
    dfs(0, nums, [], res, visited)
    return res
