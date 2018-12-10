class Solution(object):
  def generateTrees(self, n):
    """
    :type n: int
    :rtype: List[TreeNode]
    """

    def clone(root, offset):
      if root:
        newRoot = TreeNode(root.val + offset)
        left = clone(root.left, offset)
        right = clone(root.right, offset)
        newRoot.left = left
        newRoot.right = right
        return newRoot

    if not n:
      return []
    dp = [[]] * (n + 1)
    dp[0] = [None]
    for i in range(1, n + 1):
      dp[i] = []
      for j in range(1, i + 1):
        for left in dp[j - 1]:
          for right in dp[i - j]:
            root = TreeNode(j)
            root.left = left
            root.right = clone(right, j)
            dp[i].append(root)
    return dp[-1]
