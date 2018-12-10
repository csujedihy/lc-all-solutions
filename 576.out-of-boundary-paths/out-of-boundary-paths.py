class Solution(object):
  def findPaths(self, m, n, N, x, y):
    dp = [[[0] * n for _ in range(m)] for _ in range(N + 1)]
    dp[0][x][y] = 1
    ans = 0
    mod = 10 ** 9 + 7
    for k in range(1, N + 1):
      for i in range(m):
        for j in range(n):
          if i == 0:
            ans += dp[k - 1][i][j] % mod
          if i == m - 1:
            ans += dp[k - 1][i][j] % mod
          if j == 0:
            ans += dp[k - 1][i][j] % mod
          if j == n - 1:
            ans += dp[k - 1][i][j] % mod
          if i > 0:
            dp[k][i][j] += dp[k - 1][i - 1][j]
          if i < m - 1:
            dp[k][i][j] += dp[k - 1][i + 1][j]
          if j > 0:
            dp[k][i][j] += dp[k - 1][i][j - 1]
          if j < n - 1:
            dp[k][i][j] += dp[k - 1][i][j + 1]
    return ans % mod
