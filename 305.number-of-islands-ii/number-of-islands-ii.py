class UnionFind(object):
    def __init__(self, m, n):
        self.dad = [i for i in range(m * n)]
        self.rank = [0 for _ in range(m * n)]
        
    def find(self, x):
        if self.dad[x] != x:
            self.dad[x] = self.find(self.dad[x])
        return self.dad[x]
    
    def union(self, xy):
        x, y = map(self.find, xy)
        if x == y:
            return False
        if self.rank[x] > self.rank[y]:
            self.dad[y] = x
        elif self.rank[x] < self.rank[y]:
            self.dad[x] = y
        else:
            self.dad[y] = x
            self.rank[x] += 1
        return True

class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        uf = UnionFind(m, n)
        ans = 0
        ret = []
        dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        grid = set()
        for i, j in positions:
            ans += 1
            grid |= {(i, j)}
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) in grid:
                    if uf.union((ni * n + nj, i * n + j)):
                        ans -= 1
            ret.append(ans)
        return ret
        
        