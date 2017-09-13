class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(candidates, start, target, path, res):
            if target == 0:
                return res.append(path + [])
            
            for i in range(start, len(candidates)):
                if target - candidates[i] >= 0:
                    path.append(candidates[i])
                    dfs(candidates, i, target - candidates[i], path, res)
                    path.pop()
        res = []
        dfs(candidates, 0, target, [], res)
        return res