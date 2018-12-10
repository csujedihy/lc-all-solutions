# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def rob(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """

    def dfs(root):
      if not root:
        return 0, 0
      lpre, lppre = dfs(root.left)
      rpre, rppre = dfs(root.right)
      return max(root.val + lppre + rppre, lpre + rpre), lpre + rpre

    return dfs(root)[0]
