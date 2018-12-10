# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  # @param {TreeNode} root
  # @return {string[]}
  def binaryTreePaths(self, root):
    def helper(root, path, res):
      if root:
        path.append(str(root.val))
        left = helper(root.left, path, res)
        right = helper(root.right, path, res)
        if not left and not right:
          res.append("->".join(path))
        path.pop()
        return True

    res = []
    helper(root, [], res)
    return res
