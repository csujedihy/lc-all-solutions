class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(M)
        n = len(M[0])
        ans = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                cnt = 0
                sums = 0
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        newi, newj = i + di, j + dj
                        if 0 <= newi < m and 0 <= newj < n:
                            cnt += 1
                            sums += M[newi][newj]
                ans[i][j] = sums / cnt
        return ans
                        