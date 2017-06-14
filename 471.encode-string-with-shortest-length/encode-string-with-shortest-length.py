class Solution(object):
    def encode(self, s, dp = {}):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 5:
            return s
        elif s in dp:
            return dp[s]
        dp[s] = s
        idx = (2 * s).find(s, 1)
        if 0 <= idx < len(s):
            dp[s] = str(len(s) / idx) + "[" + self.encode(s[:idx], dp) + "]"
        for i in range(1, len(s)):
            left = self.encode(s[:i], dp)
            right = self.encode(s[i:], dp)
            if len(left) + len(right) < len(dp[s]):
                dp[s] = left + right
        return dp[s]
