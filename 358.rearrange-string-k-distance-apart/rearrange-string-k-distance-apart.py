class Solution(object):
    def rearrangeString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k < 2:
            return s
        d = collections.Counter(s)
        heap = [(-d[key], key) for key in d]
        heapq.heapify(heap)
        ans = []
        while len(ans) < len(s):
            temp = []
            for _ in range(k):
                if not heap:
                    return ""
                freq, c = heapq.heappop(heap)
                freq += 1
                ans.append(c)
                if len(ans) == len(s):
                    return "".join(ans)
                if freq < 0:
                    temp.append((freq, c))
            for freq, c in temp:
                heapq.heappush(heap, (freq, c))   
        return "".join(ans)