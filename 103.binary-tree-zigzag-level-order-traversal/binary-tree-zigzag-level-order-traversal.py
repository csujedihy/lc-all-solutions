# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution(object):
  def zigzagLevelOrder(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    stack = deque([root])
    ans = []
    odd = True
    while stack:
      level = []
      for k in range(0, len(stack)):
        top = stack.popleft()
        if top is None:
          continue
        level.append(top.val)
        stack.append(top.left)
        stack.append(top.right)
      if level:
        if odd:
          ans.append(level)
        else:
          ans.append(level[::-1])
      odd = not odd
    return ans
