# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution(object):
  def levelOrder(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if not root:
      return []
    ans = [[root.val]]
    queue = deque([root])
    while queue:
      levelans = []
      for _ in range(0, len(queue)):
        root = queue.popleft()
        if root.left:
          levelans.append(root.left.val)
          queue.append(root.left)
        if root.right:
          levelans.append(root.right.val)
          queue.append(root.right)
      if levelans:
        ans.append(levelans)
    return ans
