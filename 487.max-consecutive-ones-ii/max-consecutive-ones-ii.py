class Solution(object):
    def __init__(self):
        self.ans = 0
        self.count = 0
        self.lastCount = 0
        
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for num in nums:
            self.readNum(num)    # stream the input
        return self.ans
    
    def readNum(self, num):
        """
        :type nums: int
        """
        if num == 1:
            self.count += 1
        else:
            self.count = self.count - self.lastCount + 1
            self.lastCount = self.count 
        self.ans = max(self.ans, self.count)