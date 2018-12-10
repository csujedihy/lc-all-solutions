# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def buildTree(self, inorder, postorder):
    """
    :type inorder: List[int]
    :type postorder: List[int]
    :rtype: TreeNode
    """
    if inorder and postorder:
      postorder.reverse()
      self.index = 0
      d = {}
      for i in range(0, len(inorder)):
        d[inorder[i]] = i
      return self.dfs(inorder, postorder, 0, len(postorder) - 1, d)

  def dfs(self, inorder, postorder, start, end, d):
    if start <= end:
      root = TreeNode(postorder[self.index])
      mid = d[postorder[self.index]]
      self.index += 1
      root.right = self.dfs(inorder, postorder, mid + 1, end, d)
      root.left = self.dfs(inorder, postorder, start, mid - 1, d)
      return root
