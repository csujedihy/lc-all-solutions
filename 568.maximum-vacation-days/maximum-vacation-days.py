class Solution(object):
  def maxVacationDays(self, flights, days):
    """
    :type flights: List[List[int]]
    :type days: List[List[int]]
    :rtype: int
    """
    ans = 0
    dp = [[float("-inf")] * len(flights) for _ in range(2)]
    dp[0][0] = 0
    for i in range(len(days[0])):
      for j in range(len(flights)):
        for k in range(len(flights)):
          if flights[k][j] == 1 or j == k:
            dp[(i + 1) % 2][j] = max(dp[(i + 1) % 2][j], dp[i % 2][k] + days[j][i])
    return max(dp[len(days[0]) % 2])
