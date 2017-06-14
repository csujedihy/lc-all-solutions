class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def dfs(left, path, res, n):
            if len(path) == 2 * n:
                if left == 0:
                    res.append("".join(path))
                return
            
            if left < n:
                path.append("(")
                dfs(left + 1, path, res, n)
                path.pop()
            if left > 0:
                path.append(")")
                dfs(left - 1, path, res, n)
                path.pop()
            
        res = []
        dfs(0, [], res, n)
        return res