# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def boundaryOfBinaryTree(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if not root:
      return []

    def dfsLeft(root, res):
      if not root or (not root.left and not root.right):
        return
      res.append(root.val)
      if root.left:
        dfsLeft(root.left, res)
      else:
        dfsLeft(root.right, res)

    def dfsRight(root, res):
      if not root or (not root.left and not root.right):
        return
      if root.right:
        dfsRight(root.right, res)
      else:
        dfsRight(root.left, res)
      res.append(root.val)

    def dfsLeaves(root, res, mid):
      if not root:
        return
      if not root.left and not root.right and root != mid:
        res.append(root.val)
      dfsLeaves(root.left, res, mid)
      dfsLeaves(root.right, res, mid)

    res = [root.val]
    dfsLeft(root.left, res)
    dfsLeaves(root, res, root)
    dfsRight(root.right, res)
    return res
