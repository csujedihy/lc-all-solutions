import collections


class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        sumLen = sum(nums)
        if sumLen % 4 != 0:
            return False
        self.sideLen = sideLen = sumLen / 4
        for side in nums:
            if side > sideLen:
                return False
        halfLen = 2 * sideLen
        sticksIdx = set([i for i in range(0, len(nums))])
        nums.sort()
        
        def backpack(nums, subset):
            cands = [nums[k] for k in subset]
            dp = [[False] * (self.sideLen + 1) for _ in range(len(cands))]
            for i in range(0, len(cands)):
                dp[i][0] = True
            for i in range(0, len(cands)):
                for j in range(1, self.sideLen + 1):
                    dp[i][j] |= dp[i - 1][j]
                    if j - cands[i] >= 0:
                        dp[i][j] |= dp[i - 1][j - cands[i]]
            return dp[-1][-1]

        def dfs(nums, start, sticksIdx, halfLen, subSum, subsetIdx):
            if subSum >= halfLen:
                if subSum == halfLen and backpack(nums, subsetIdx) and backpack(nums, sticksIdx):
                    return True
                return False

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                if i in sticksIdx:
                    sticksIdx -= {i}
                    subsetIdx |= {i}
                    if dfs(nums, i + 1, sticksIdx, halfLen, subSum + nums[i], subsetIdx):
                        return True
                    subsetIdx -= {i}
                    sticksIdx |= {i}
            return False

        return dfs(nums, 0, sticksIdx, halfLen, 0, set())