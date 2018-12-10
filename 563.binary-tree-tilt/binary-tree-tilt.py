# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def findTilt(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """

    def dfs(root):
      if not root:
        return 0, 0  # sum, tilt sum

      leftSum, leftTilt = dfs(root.left)
      rightSum, rightTilt = dfs(root.right)

      return leftSum + root.val + rightSum, abs(leftSum - rightSum) + leftTilt + rightTilt

    return dfs(root)[1]
