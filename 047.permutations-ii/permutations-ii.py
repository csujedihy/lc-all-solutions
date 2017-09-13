class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        def dfs(nums, res, path, visited):
            if len(path) == len(nums):
                res.append(path + [])
                return
            
            for i in range(len(nums)):
                if i in visited:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and i - 1 not in visited:
                    continue
                visited |= {i}
                path.append(nums[i])
                dfs(nums, res, path, visited)
                path.pop()
                visited -= {i}
            
        dfs(nums, res, [], set())
        return res