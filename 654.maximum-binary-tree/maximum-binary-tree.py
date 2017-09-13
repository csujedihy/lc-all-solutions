# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # recursion
    def _constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums:
            pos = nums.index(max(nums))
            root = TreeNode(nums[pos])
            root.left = self.constructMaximumBinaryTree(nums[:pos])
            root.right = self.constructMaximumBinaryTree(nums[pos+1:])
            return root
        
    # decreasing stack
    def constructMaximumBinaryTree(self, nums):
        stack = []
        for num in nums:
            root = TreeNode(num)
            while stack and stack[-1].val < num:
                root.left = stack.pop()
            if stack:
                stack[-1].right = root
            stack.append(root)
        return stack and stack[0]
            
            
            
            
            