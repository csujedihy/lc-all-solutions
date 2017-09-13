"""
1. group operations as ([^C][^V][^V]...[^V]) that has in total k operations and it gets k * # of A
2. n can be written as x_1 * x_2 * ... * x_N
3. then total operations # = x_1 + x_2 + ... + x_N
4. since p * q >= p + q for integers > 1, to min the result
5. decomposite x_1 to x_N to min the sum
"""
    
class Solution(object):
    def _minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        for i in range(2, int((n + 1)**0.5) + 1):
            if n % i == 0:
                return i + self.minSteps(n / i)
        return n
        
    def minSteps(self, n):
        def factor(n):
            d = 2
            while d * d <= n:
                while n % d == 0:
                    n /= d
                    yield d
                d += 1
            if n > 1:
                yield n
        return sum(factor(n))
                
                
                
            