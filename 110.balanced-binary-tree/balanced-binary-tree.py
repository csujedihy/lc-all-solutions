# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def isBalanced(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """

    def dfs(p):
      if not p:
        return 0

      left = dfs(p.left)
      right = dfs(p.right)
      if left == -1 or right == -1:
        return -1
      if abs(left - right) > 1:
        return -1
      return 1 + max(left, right)

    if dfs(root) == -1:
      return False
    return True
