# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l < r:
            m = l + (r - l) / 2
            if isBadVersion(m):
                r = m - 1
            else:
                l = m + 1
        
        if not isBadVersion(r):
            return r + 1
        return r
                