class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes.sort(key=lambda key:(key[0], -key[1]))
        tails = []
        for i in xrange(0, len(envelopes)):
            idx = bisect.bisect_right(tails, envelopes[i][1])
            if idx - 1 >= 0 and tails[idx - 1] == envelopes[i][1]:
                continue
            if idx == len(tails):
                tails.append(envelopes[i][1])
            else:
                tails[idx] = envelopes[i][1]
        return len(tails)