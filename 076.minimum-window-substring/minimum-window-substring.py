from collections import deque
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        minLen = len(s) + 1
        start, end = None, None
        deq = deque([])
        fullscore = len(t)
        d = {}
        cd = {}
        for ltr in t:
            d[ltr] = d.get(ltr, 0) + 1
        score = 0
        for i in xrange(0, len(s)):
            if s[i] not in d:
                continue
            if s[i] in d:
                deq.append(i)
                cd[s[i]] = cd.get(s[i], 0) + 1
                if cd[s[i]] <= d[s[i]] and score < fullscore:
                    score += 1
                while deq and cd[s[deq[0]]] > d[s[deq[0]]]:
                    cd[s[deq[0]]] -= 1
                    deq.popleft()
                if score == fullscore:
                    if deq[-1] - deq[0] + 1 < minLen:
                        minLen = deq[-1] - deq[0] + 1
                        start, end = deq[0], deq[-1]

        if score == fullscore:
            return s[start:end+1]
        return ""
        
        