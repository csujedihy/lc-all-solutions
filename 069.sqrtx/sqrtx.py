class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        lo = 0
        hi = x
        while lo <= hi:
            mid = (hi + lo) / 2
            v = mid * mid
            if v < x:
                lo = mid + 1
            elif v > x:
                hi = mid - 1
            else:
                return mid
        return hi