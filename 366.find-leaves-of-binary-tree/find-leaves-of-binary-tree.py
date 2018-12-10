# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections


class Solution(object):
  def findLeaves(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """

    def helper(p, res):
      if not p:
        return 0
      left = helper(p.left, res)
      right = helper(p.right, res)
      depth = max(left, right) + 1
      res[depth].append(p.val)
      return depth

    ans = []
    res = collections.defaultdict(list)
    helper(root, res)
    for i in range(1, len(res) + 1):
      ans.append(res[i])
    return ans
