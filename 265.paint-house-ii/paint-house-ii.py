class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0
        dp = [[0] * len(costs[0]) for _ in xrange(0, len(costs))]
        dp[0] = costs[0]
        for i in xrange(1, len(costs)):
            for j in xrange(0, len(costs[0])):
                dp[i][j] = min(dp[i - 1][:j] + dp[i - 1][j + 1:]) + costs[i][j]
        return min(dp[-1])