# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def closestValue(self, p, target):
    """
    :type root: TreeNode
    :type target: float
    :rtype: int
    """
    ans = p.val
    while p:
      if abs(target - p.val) < abs(ans - target):
        ans = p.val
      if target < p.val:
        p = p.left
      else:
        p = p.right
    return ans
