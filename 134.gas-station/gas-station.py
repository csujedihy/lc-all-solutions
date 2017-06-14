class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        totalgas = 0
        totalcost = 0
        start = 0
        balance = 0
        for i in xrange(0, len(gas)):
            totalgas += gas[i]
            totalcost += cost[i]

        for i in range(0, len(gas)):
            balance += gas[i] - cost[i]
            if balance < 0:
                start = i + 1
                balance = 0

        if totalcost <= totalgas:
            return start
        return -1