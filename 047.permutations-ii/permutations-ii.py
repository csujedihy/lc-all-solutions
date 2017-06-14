class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        visited = [False] * len(nums)
        def dfs(nums, path, res, visited):
            if len(path) == len(nums):
                res.append(path + [])
                return
            
            for i in xrange(0, len(nums)):
                if visited[i]:
                    continue
                if i > 0 and nums[i - 1] == nums[i] and not visited[i-1]:
                    continue
                visited[i] = True
                path.append(nums[i])
                dfs(nums, path, res, visited)
                path.pop()
                visited[i] = False
                    
        dfs(nums, [], res, visited)
        return res
            