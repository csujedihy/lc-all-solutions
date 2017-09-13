class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        tails = []
        for start, end in sorted(pairs):
            idx = bisect.bisect_left(tails, start)
            if idx == len(tails):
                tails.append(end)
            else:
                tails[idx] = min(tails[idx], end)
        return len(tails)
            