class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        l = len(n)
        cands = set([str(10**l + 1), str(10**(l-1) - 1)])
        prefix = int(n[:(l + 1) / 2])
        for half in map(str, [prefix - 1, prefix, prefix + 1]):
            cands.add(half + [half, half[:-1]][l & 1][::-1])
        cands.discard(n)
        return min(cands, key = lambda x: (abs(int(x) - int(n)), int(x)))