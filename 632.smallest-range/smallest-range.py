from collections import deque
class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        k = len(nums)
        d = collections.defaultdict(int)
        tuples = []

        for i in range(len(nums)):
            for num in nums[i]:
                tuples.append((num, i))

        tuples.sort()
        length = len(tuples)
        left = tuples[0][0]
        right = tuples[-1][0]
        deq = deque([])
        for i in range(length):
            num, no = tuples[i]
            deq.append(tuples[i])
            d[no] += 1
            while len(deq) > 1 and d[deq[0][1]] > 1:
                _num, _no = deq.popleft()
                d[_no] -= 1
                if d[_no] == 0:
                    del d[_no]
            if len(d) == k:
                l, r = deq[0][0], deq[-1][0]
                if r - l < right - left:
                    left = l
                    right = r
        return (left, right)