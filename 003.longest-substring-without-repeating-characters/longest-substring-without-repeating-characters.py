class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        cset = set([])
        j = 0
        ans = 0
        for i in xrange(0, len(s)):
            while j < len(s) and s[j] not in cset:
                cset.add(s[j])
                j += 1
            
            ans = max(ans, j - i)
            cset.discard(s[i])
            
        return ans