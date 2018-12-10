# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def largestValues(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    ans = []
    d = {}

    def dfs(root, h, d):
      if root:
        dfs(root.left, h + 1, d)
        dfs(root.right, h + 1, d)
        d[h] = max(d.get(h, float("-inf")), root.val)

    dfs(root, 0, d)
    level = 0
    while level in d:
      ans += d[level],
      level += 1
    return ans
