import heapq
import collections
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        total = len(tasks)
        cache = {}
        heap = []
        ans = 0
        d = collections.Counter(tasks)
        for k, v in d.iteritems():
            heap.append((-v, k))
        heapq.heapify(heap)

        while heap:
            count, task = heap[0]
            stack = []
            if task not in cache or ans - cache[task] > n:
                heapq.heappop(heap)
                total -= 1
                cache[task] = ans
                ans += 1
                for _ in range(n):
                    if heap:
                        c, t = heapq.heappop(heap)
                        if t not in cache or ans - cache[t] > n:
                            total -= 1
                            cache[t] = ans
                        if c < -1:
                            stack.append((c + 1, t))
                    elif total == 0:
                        return ans
                    ans += 1
                while stack:
                    heapq.heappush(heap, stack.pop())
                if count < -1:
                    heapq.heappush(heap, (count + 1, task))
            else:
                ans += 1
        return ans