# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def pathSum(self, root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: List[List[int]]
    """

    def dfs(root, s, path, res):
      if root:
        path.append(root.val)
        s -= root.val
        left = dfs(root.left, s, path, res)
        right = dfs(root.right, s, path, res)
        if not left and not right and s == 0:
          res.append(path + [])
        path.pop()
        return True

    res = []
    dfs(root, sum, [], res)
    return res
