# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def sortedArrayToBST(self, nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    if nums:
      midPos = len(nums) / 2
      mid = nums[midPos]
      root = TreeNode(mid)
      root.left = self.sortedArrayToBST(nums[:midPos])
      root.right = self.sortedArrayToBST(nums[midPos + 1:])
      return root
