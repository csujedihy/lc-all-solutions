class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, x, y, num, dmin, dmax):
            if root:
                left = dfs(root.left, x - 1, y + 1, num * 2, dmin, dmax)
                right = dfs(root.right, x + 1, y + 1, 1 + num * 2, dmin, dmax)
                dmin[y] = min(num, dmin.get(y, float("inf")))
                dmax[y] = max(num, dmax.get(y, float("-inf")))
                return max(left or 0, right or 0, 1 + dmax[y] - dmin[y])
        return dfs(root, 0, 0, 1, {}, {})
            
            