class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        m = 1
        ones = 0
        while m <= n:
            r = (n / m) % 10
            if r > 1:
                ones += m
            elif r == 1:
                ones += n % m + 1                

            ones += (n / (m * 10)) * m
            m *= 10
        return ones