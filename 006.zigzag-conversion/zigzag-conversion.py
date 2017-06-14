class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if not s or numRows == 0:
            return ""
        if numRows == 1:
            return s
        ans = ""
        step = numRows * 2 - 2
        for i in xrange(0, numRows):
            if i == 0 or i == numRows - 1:
                for j in xrange(i, len(s), step):
                    ans += s[j]
            else:
                for j in xrange(i, len(s), step):
                    ans += s[j]
                    if j + step - 2 * i < len(s):
                        ans += s[j + step - 2 * i]
        return ans
                    
            