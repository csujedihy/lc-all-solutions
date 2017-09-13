class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = collections.defaultdict(list)
        for num in nums:
            if d[num - 1]:
                heapq.heappush(d[num], heapq.heappop(d[num - 1]) + 1)
            else:
                heapq.heappush(d[num], 1)
        return not any(length < 3 for length in sum(d.values(), []))
                
        