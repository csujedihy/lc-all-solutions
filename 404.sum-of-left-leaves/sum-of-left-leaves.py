# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def sumOfLeftLeaves(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """

    def helper(root, isLeft):
      if not root:
        return None
      left = helper(root.left, True)
      right = helper(root.right, False)
      ret = 0
      if left is None and right is None and isLeft:
        return root.val
      if left:
        ret += left
      if right:
        ret += right
      return ret

    ret = helper(root, False)
    if ret:
      return ret
    return 0
