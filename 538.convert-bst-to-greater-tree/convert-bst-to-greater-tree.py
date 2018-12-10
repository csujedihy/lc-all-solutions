# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def __init__(self):
    self.lSum = 0

  def convertBST(self, root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if not root:
      return None
    self.convertBST(root.right)
    self.lSum += root.val
    root.val = self.lSum
    self.convertBST(root.left)
    return root
