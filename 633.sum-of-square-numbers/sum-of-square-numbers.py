class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        n = int(c ** 0.5)
        start = 0
        end = n
        while start <= end:
            mid = start ** 2 + end ** 2
            if mid == c:
                return True
            elif mid < c:
                start += 1
            else:
                end -= 1
        return False
            