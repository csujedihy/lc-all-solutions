directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        def dfs(matrix, i, j, visited, cache):
            if (i, j) in visited:
                return visited[(i, j)]
                
            ret = 0
            for di, dj in directions:
                p, q = i + di, j + dj
                if p < 0 or q < 0 or p >= len(matrix) or q >= len(matrix[0]):
                    continue
                if (p, q) not in cache and matrix[p][q] > matrix[i][j]:
                    cache.add((p, q))
                    r = dfs(matrix, p, q, visited, cache)
                    ret = max(ret, r)
                    cache.discard((p, q))
                    
            visited[(i, j)] = ret + 1
            return ret + 1
            
        visited = {}
        cache = set()
        ans = 0
        for i in xrange(0, len(matrix)):
            for j in xrange(0, len(matrix[0])):
                cache.add((i, j))
                ans = max(ans, dfs(matrix, i, j, visited, cache))
                cache.discard((i, j))
        return ans