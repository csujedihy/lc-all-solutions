class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxlen = 0
        maxcoord = None
        for i in xrange(0, len(s)):
            if 2*(len(s) - i) + 1 < maxlen:
                break
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1> maxlen:
                    maxlen = r - l + 1
                    maxcoord = (l, r)
                l -= 1
                r += 1
            
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1> maxlen:
                    maxlen = r - l + 1
                    maxcoord = (l, r)
                l -= 1
                r += 1
                    
        
        return s[maxcoord[0]:maxcoord[1] + 1] if maxcoord else ""
                