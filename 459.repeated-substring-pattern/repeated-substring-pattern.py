class Solution(object):

    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        for i in xrange(0, len(str) / 2):
            if not len(str) % (i + 1) and str[:i+1] * (len(str) / (i+1)) == str:
                return True
        return False