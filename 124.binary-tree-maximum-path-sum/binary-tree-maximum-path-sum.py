# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def maxPathSum(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """

    def dfs(root):
      if not root: return (0, float("-inf"))
      (l, lm), (r, rm) = map(dfs, [root.left, root.right])
      return (max(root.val, root.val + max(l, r)), max(lm, rm, root.val + max(l, r), root.val, root.val + l + r))

    return dfs(root)[1]
