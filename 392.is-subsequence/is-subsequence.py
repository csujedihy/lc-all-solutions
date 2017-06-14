class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = collections.defaultdict(list)
        for i, c in enumerate(t):
            d[c].append(i)
        start = 0
        for c in s:
            idx = bisect.bisect_left(d[c], start)
            if len(d[c]) == 0 or idx >= len(d[c]):
                return False
            start = d[c][idx] + 1
        return True