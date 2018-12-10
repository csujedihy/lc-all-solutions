# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def getMinimumDifference(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    self.val = None
    self.ans = float("inf")

    def inorder(root):
      if not root:
        return
      inorder(root.left)
      if self.val is not None:
        self.ans = min(self.ans, abs(root.val - self.val))
      self.val = root.val
      inorder(root.right)

    inorder(root)
    return self.ans
