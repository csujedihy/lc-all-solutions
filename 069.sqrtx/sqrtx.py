class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        start, end = 0, x
        while start <= end:
            mid = start + ((end - start) >> 2)            
            value = mid * mid
            if value > x:
                end = mid - 1
            elif value <= x:
                start = mid + 1
        return end