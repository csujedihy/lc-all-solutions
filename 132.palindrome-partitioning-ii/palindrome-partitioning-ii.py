class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        pal = [[False for j in xrange(0, len(s))] for i in xrange(0, len(s))]
        dp = [len(s) for _ in xrange(0, len(s) + 1)]
        for i in xrange(0, len(s)):
            for j in xrange(0, i + 1):
                if (s[i] == s[j]) and ((j + 1 > i - 1) or (pal[i - 1][j + 1])):
                    pal[i][j] = True
                    dp[i+1] = min(dp[i+1], dp[j] + 1) if j != 0 else 0
        return dp[-1]