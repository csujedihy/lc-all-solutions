class Solution(object):
  def pathSum(self, root, target):
    """
    :type root: TreeNode
    :type target: int
    :rtype: int
    """
    self.count = 0
    preDict = {0: 1}

    def dfs(p, target, pathSum, preDict):
      if p:
        pathSum += p.val
        self.count += preDict.get(pathSum - target, 0)
        preDict[pathSum] = preDict.get(pathSum, 0) + 1
        dfs(p.left, target, pathSum, preDict)
        dfs(p.right, target, pathSum, preDict)
        preDict[pathSum] -= 1

    dfs(root, target, 0, preDict)
    return self.count
