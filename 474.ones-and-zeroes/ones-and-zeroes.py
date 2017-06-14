class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n + 1) for _ in range(0, m + 1)]
        for dj, dk in [(s.count("0"), s.count("1")) for s in strs]:
            for j in reversed(range(0, m + 1)):
                for k in reversed(range(0, n + 1)):
                    if j - dj >= 0 and k - dk >= 0:
                        dp[j][k] = max(dp[j][k], dp[j - dj][k - dk] + 1)
        return dp[-1][-1]