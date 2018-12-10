# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def findBottomLeftValue(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """

    def dfs(root, h, w):
      if not root:
        return (float("inf"), float("inf"), None)
      left = dfs(root.left, h - 1, w - 1)
      right = dfs(root.right, h - 1, w + 1)
      return min((h, w, root.val), left, right)

    return dfs(root, 0, 0)[2]
