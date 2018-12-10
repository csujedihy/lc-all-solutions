# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def postorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    res, stack = [], [(1, root)]
    while stack:
      p = stack.pop()
      if not p[1]:
        continue
      if p[0] == 0:
        res.append(p[1].val)
      else:
        stack.extend([(0, p[1]), (1, p[1].right), (1, p[1].left)])
    return res
