# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution(object):
  def rightSideView(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """

    def dfs(root, h):
      if root:
        if h == len(ans):
          ans.append(root.val)
        dfs(root.right, h + 1)
        dfs(root.left, h + 1)

    ans = []
    dfs(root, 0)
    return ans
