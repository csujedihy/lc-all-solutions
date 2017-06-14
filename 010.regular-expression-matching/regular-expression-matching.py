class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p) > 0 and p[0] == "*":
            return False
            
        dp = [[False] * (len(p) + 1) for i in range(2)]
        dp[0][0] = True
            
        for j in xrange(1, len(p) + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 2]

        for i in xrange(1, len(s) + 1):
            if i > 1:
                dp[0][0] = False
            for j in xrange(1, len(p) + 1):
                if p[j - 1] != "*":
                    dp[i%2][j] = (dp[(i - 1)%2][j - 1] and (p[j - 1] == "." or s[i - 1] == p[j - 1]))
                else:
                    dp[i%2][j] = dp[i%2][j - 2] or dp[i%2][j - 1]
                    if p[j - 2] == s[i - 1] or p[j - 2] == ".":
                        dp[i%2][j] |= dp[(i - 1)%2][j]
        return dp[len(s) % 2][-1]
        