import collections
import heapq
class Solution(object):
    def rearrangeString(self, str, k):
        """
        :type str: str
        :type k: int
        :rtype: str
        """
        ans = []
        count = collections.Counter(str)
        posDict = {}
        heap = []
        for key in count:
            heapq.heappush(heap, (-count[key], key))
        while len(ans) < len(str):
            freq, key = heapq.heappop(heap)
            ans += key,
            stack = []
            for _ in range(k - 1):
                if len(str) == len(ans):
                    return "".join(ans)
                if not heap:
                    return ""
                _freq, _key = heapq.heappop(heap)
                ans += _key,
                if _freq < -1:
                    stack.append((_freq + 1, _key))
            while stack:
                heapq.heappush(heap, stack.pop())
            heapq.heappush(heap, (freq + 1, key))
        return "".join(ans)
        