# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def isSymmetric(self, node):
    """
    :type root: TreeNode
    :rtype: bool
    """

    def helper(root, mirror):
      if not root and not mirror:
        return True
      if root and mirror and root.val == mirror.val:
        return helper(root.left, mirror.right) and helper(root.right, mirror.left)
      return False

    return helper(node, node)
