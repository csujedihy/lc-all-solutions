class Solution(object):
  def minCost(self, costs):
    """
    :type costs: List[List[int]]
    :rtype: int
    """
    if not costs:
      return 0
    dp = [0] * (len(costs[0]))
    dp[:] = costs[0]
    for i in range(1, len(costs)):
      d0 = d1 = d2 = 0
      for j in range(0, 3):
        if j == 0:
          d0 = min(dp[1], dp[2]) + costs[i][0]
        elif j == 1:
          d1 = min(dp[0], dp[2]) + costs[i][1]
        else:
          d2 = min(dp[0], dp[1]) + costs[i][2]
      dp[0], dp[1], dp[2] = d0, d1, d2
    return min(dp)
