# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def inorderSuccessor(self, root, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :rtype: TreeNode
    """
    if root and q:
      flag = False
      stack = [(1, root)]
      while stack:
        p = stack.pop()
        if not p[1]:
          continue
        if p[0] == 0:
          if flag:
            return p[1]
          if p[1] == q:
            flag = True
        else:
          stack.extend([(1, p[1].right), (0, p[1]), (1, p[1].left)])

      return None
