# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        def height(root):
            if not root:
                return 0
            return 1 + max(height(root.left), height(root.right))
        
        def fill(root, res, left, right, h):
            if root:
                val = str(root.val)
                mid = left + (right - left) / 2
                res[h][mid] = val
                fill(root.left, res, left, mid - 1, h + 1)
                fill(root.right, res, mid + 1, right, h + 1)
            
        
        h = height(root)
        res = [[""] * (2**h - 1) for _ in range(h)]
        fill(root, res, 0, len(res[0]) - 1, 0)
        return res
        