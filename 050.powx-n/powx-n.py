class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1 / x
            n = -n
            
        ans = 1
        while n > 0:
            if n & 0x01:
                ans *= x
            x *= x
            n >>= 1
        return ans
            