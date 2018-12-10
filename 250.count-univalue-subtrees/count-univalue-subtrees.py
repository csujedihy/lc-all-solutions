# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def countUnivalSubtrees(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    self.count = 0

    def dfs(root, pv):
      if not root:
        return True
      left = dfs(root.left, root.val)
      right = dfs(root.right, root.val)
      if left and right:
        self.count += 1
        if root.val == pv:
          return True
      return False

    if root:
      dfs(root, root.val)
    return self.count
