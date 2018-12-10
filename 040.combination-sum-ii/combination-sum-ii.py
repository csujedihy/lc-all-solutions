class Solution(object):
  def combinationSum2(self, candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """

    def dfs(nums, target, start, visited, path, res):
      if target == 0:
        res.append(path + [])
        return

      for i in range(start, len(nums)):
        if i > start and nums[i] == nums[i - 1]:
          continue
        if target - nums[i] < 0:
          return 0
        if i not in visited:
          visited.add(i)
          path.append(nums[i])
          dfs(nums, target - nums[i], i + 1, visited, path, res)
          path.pop()
          visited.discard(i)

    candidates.sort()
    res = []
    visited = set([])
    dfs(candidates, target, 0, visited, [], res)
    return res
