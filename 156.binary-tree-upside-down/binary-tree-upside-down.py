# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def upsideDownBinaryTree(self, root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if not root:
      return

    left = self.upsideDownBinaryTree(root.left)
    right = self.upsideDownBinaryTree(root.right)
    if root.left:
      root.left.right = root
      root.left.left = root.right
      root.left = root.right = None
    return left if left else root
