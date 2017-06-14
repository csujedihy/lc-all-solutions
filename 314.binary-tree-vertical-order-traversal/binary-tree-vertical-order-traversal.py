from collections import defaultdict
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def dfs(p, i, j, res):
            if p:
                res[j].append((p.val, i))
                self.leftMost = min(j, self.leftMost)
                dfs(p.left, i + 1, j - 1, res)
                dfs(p.right, i + 1, j + 1, res)
                
        self.leftMost = float("inf")
        ans = []
        res = defaultdict(list)
        dfs(root, 0, 0, res)
        i = self.leftMost
        while True:
            if not res[i]:
                break
            ans.append([item[0] for item in sorted(res[i], key=lambda a:a[1])])
            i += 1
        return ans