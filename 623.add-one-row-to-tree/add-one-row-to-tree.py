# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def addOneRow(self, root, v, d):
    """
    :type root: TreeNode
    :type v: int
    :type d: int
    :rtype: TreeNode
    """
    # BFS is even better because it terminates much earlier
    dummy = TreeNode(-1)
    dummy.left = root
    stack = [(1, dummy, 0)]
    while stack:
      p, node, h = stack.pop()
      if not node:
        continue
      if p == 1:
        stack.extend([(1, node.right, h + 1), (1, node.left, h + 1), (0, node, h + 1)])
      elif h == d:
        left = node.left
        right = node.right
        node.left, node.right = map(TreeNode, (v, v))
        node.left.left = left
        node.right.right = right
    return dummy.left
