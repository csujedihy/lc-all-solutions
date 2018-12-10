# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def largestBSTSubtree(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """

    def helper(root):
      if not root:
        return (0, 0, float("inf"), float("-inf"))  # numBST, maxNumBST, min, max
      lnumBST, lmaxNumBST, lmin, lmax = helper(root.left)
      rnumBST, rmaxNumBST, rmin, rmax = helper(root.right)
      numBST = -1
      if lmax < root.val < rmin and lnumBST != -1 and rnumBST != -1:
        numBST = 1 + lnumBST + rnumBST
      maxNumBST = max(1, lmaxNumBST, rmaxNumBST, numBST)
      return numBST, maxNumBST, min(lmin, rmin, root.val), max(lmax, rmax, root.val)

    return helper(root)[1]
