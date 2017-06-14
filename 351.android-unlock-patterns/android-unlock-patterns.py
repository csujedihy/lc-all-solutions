class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def dfs(m, n, prev, visited, length):
            if m <= length <= n:
                self.ans += 1
            
            if length == n:
                return
            
            for i in xrange(1, 10):
                if i not in visited:
                    x, y, xp, yp = (i - 1) / 3, (i - 1) % 3, (prev - 1) / 3, (prev - 1) % 3
                    if (5 not in visited and (x + xp, y + yp) == (2, 2)) or ((x == xp and abs(y - yp) == 2) or (y == yp and abs(x - xp) == 2)) and (prev + i) / 2 not in visited:
                        continue
                    visited |= {i}
                    dfs(m, n, i, visited, length + 1)
                    visited.discard(i)
        
        visited = set()
        self.ans = 0
        dfs(m, n, -99, visited, 0)
        return self.ans