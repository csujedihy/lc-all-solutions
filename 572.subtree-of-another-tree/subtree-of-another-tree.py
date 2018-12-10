# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def isSubtree(self, s, t):
    """
    :type s: TreeNode
    :type t: TreeNode
    :rtype: bool
    """

    def serialize(root):
      ans = []
      stack = [(root, 1)]
      while stack:
        node, p = stack.pop()
        if not node:
          ans.append("#")
          continue
        if p == 0:
          ans.append("|" + str(node.val))
        else:
          stack.append((node.right, 1))
          stack.append((node.left, 1))
          stack.append((node, 0))
      return ",".join(ans)

    return serialize(t) in serialize(s)
