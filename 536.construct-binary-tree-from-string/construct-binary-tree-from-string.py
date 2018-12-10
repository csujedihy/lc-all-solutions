# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def str2tree(self, s):
    """
    :type s: str
    :rtype: TreeNode
    """
    if s:
      cnt = start = 0
      root = None
      for i, c in enumerate(s):
        if c == "(":
          if not root and cnt == 0:
            root = TreeNode(s[:i])
          cnt += 1
          if cnt == 1:
            start = i + 1
        if c == ")":
          cnt -= 1
          if cnt == 0:
            if not root.left:
              root.left = self.str2tree(s[start:i])
            else:
              root.right = self.str2tree(s[start:i])
      return root if root else TreeNode(s)
