from operator import *
class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        ops = {"+": add, "-": sub, "*": mul, "/": div}
        ans = []
        for i, c in enumerate(input):
            if c in ops:
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                ans.extend([ops[c](a, b) for a in left for b in right])
        return ans if ans else [int(input)]