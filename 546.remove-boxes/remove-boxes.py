class Solution(object):
  def removeBoxes(self, A):
    N = len(A)
    memo = [[[0] * N for _ in range(N)] for _ in range(N)]

    def dp(i, j, k):
      if i > j: return 0
      if not memo[i][j][k]:
        m = i
        while m + 1 <= j and A[m + 1] == A[i]:
          m += 1
        i, k = m, k + m - i
        ans = dp(i + 1, j, 0) + (k + 1) ** 2
        for m in range(i + 1, j + 1):
          if A[i] == A[m]:
            ans = max(ans, dp(i + 1, m - 1, 0) + dp(m, j, k + 1))
        memo[i][j][k] = ans
      return memo[i][j][k]

    return dp(0, N - 1, 0)
