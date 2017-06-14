class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1
        if x < 0:
            sign = -1
            x = -x
            
        res = 0
        while x > 0:
            res *= 10
            res += x % 10
            x /= 10
            
        return sign * res if abs(res) < 0x7fffffff else 0