class Solution(object):
    def newInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        k = 1
        while n > 0:
            ans += (n % 9) * k
            k *= 10
            n /= 9
        return ans