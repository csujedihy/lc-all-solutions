class UnionFind():
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.dad = [i for i in range(m * n)]
        self.rank = [0 for i in range(m * n)]

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
        elif self.rank[y] > self.rank[x]:
            self.dad[x] = y
        else:
            self.dad[y] = x
            self.rank[x] += 1
        return True

class Solution:
    def numIslands2(self, m, n, operators):
        uf = UnionFind(m, n)
        ans = 0
        ret = []
        grid = [[0] * n for i in range(m)]
        for i, j in operators:
            ans += 1
            grid[i][j] = 1
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                newi, newj = i + di, j + dj
                if 0 <= newi < m and 0 <= newj < n and grid[newi][newj] == 1:
                    if uf.union((i*n + j, newi * n + newj)):
                        ans -= 1
            ret.append(ans)
        return ret
            
