class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        res = 0
        _x = x if x > 0 else -x
        while _x > 0:
            res = res * 10 + _x % 10
            _x /= 10
        print res, x
        return res == x