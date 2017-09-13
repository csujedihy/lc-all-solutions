# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def checkEqualTree(self, root):
        def sum(node):
            if not node:
                return 0
            s = node.val + sum(node.left) + sum(node.right)
            if node is not root:
                cuts.add(s)
            return s
        cuts = set()
        return sum(root) / 2. in cuts